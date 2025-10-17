import os
import pandas as pd
import sqlite3
from sqlalchemy import create_engine, inspect

#  Подключение к creds.db 

def load_pg_creds(sqlite_path="creds.db"):
    try:
        with sqlite3.connect(sqlite_path) as conn:
            creds = pd.read_sql_query("SELECT url, port, user, pass FROM access LIMIT 1;", conn)
        return creds.iloc[0].to_dict()
    except Exception as e:
        print(f" Ошибка при чтении creds.db: {e}")
        return None

#  Загрузка и подготовка данных 

def prepare_dataset(file_path="dataset.csv", max_rows=10):  # Уменьшил для теста
    try:
        df = pd.read_csv(file_path).head(max_rows)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        print(f" Загружено {len(df)} строк с колонками: {list(df.columns)}")
        return df
    except Exception as e:
        print(f" Ошибка при загрузке dataset.csv: {e}")
        return None

#  Запись в PostgreSQL 

def upload_to_postgres(df, creds, table_name="dolgikh_test"): 
    try:
        conn_str = f"postgresql+psycopg2://{creds['user']}:{creds['pass']}@{creds['url']}:{creds['port']}/freezone"
        print(f" Подключаемся к: {creds['url']}:{creds['port']}/freezone")
        
        engine = create_engine(conn_str, pool_recycle=3600, connect_args={'connect_timeout': 10})

        # Проверяем соединение
        with engine.connect() as test_conn:
            print(" Соединение с freezone установлено успешно!")

        # Запись данных
        with engine.begin() as conn:
            df.to_sql(
                name=table_name,
                con=conn,
                schema="public",
                if_exists="replace",  # Для теста используем replace
                index=False,
                method='multi'
            )

        # Проверка наличия таблицы
        inspector = inspect(engine)
        tables = inspector.get_table_names(schema="public")
        if table_name in tables:
            print(f" Таблица '{table_name}' успешно создана в схеме public!")
            return engine
        else:
            print(f" Таблица '{table_name}' не найдена. Текущие таблицы: {tables}")
            return None

    except Exception as e:
        print(f" Ошибка при загрузке в PostgreSQL: {e}")
        return None

#  Проверка результата 

def verify_upload(engine, table_name="dolgikh_test"):
    """Выводит 5 строк из загруженной таблицы для проверки."""
    try:
        query = f"SELECT * FROM public.{table_name} LIMIT 5"
        sample = pd.read_sql(query, con=engine)
        print("\n Первые строки загруженных данных:")
        print(sample.to_string(index=False))
        return True
    except Exception as e:
        print(f" Ошибка при проверке данных: {e}")
        return False

#  Тестовый запуск на freezone 

def test_freezone_upload():
    
    print(" ТЕСТИРУЕМ НА БАЗЕ FREEZONE")
    print("=" * 50)
    
    # Чтение учётных данных
    print(" Чтение учётных данных из creds.db")
    credentials = load_pg_creds()
    if credentials is None:
        return False
    
    # Подготовка данных (меньше строк для теста)
    print(" Подготовка датасета")
    data_sample = prepare_dataset("dataset.csv", max_rows=10)
    if data_sample is None:
        return False
    
    # Загрузка в freezone
    print(" Загрузка в PostgreSQL (freezone)")
    pg_engine = upload_to_postgres(data_sample, credentials, table_name="dolgikh_test")
    if pg_engine is None:
        return False
    
    # Проверка
    print(" Проверка результата")
    success = verify_upload(pg_engine, "dolgikh_test")
    
    if success:
        print("\n ТЕСТ УСПЕШЕН!")
        print("Теперь можно загружать в homeworks")
        return True
    else:
        print("\n ТЕСТ НЕ УДАЛСЯ.")
        return False

#  Основная программа

if __name__ == "__main__":
    # Сначала тестируем на freezone
    if test_freezone_upload():
        print("\n" + "="*50)
        response = input(" Тест успешен! Загрузить данные в homeworks? (y/n): ")
        
        if response.lower() == 'y':
            print("\n ЗАГРУЗКА В HOMEWORKS")
            print("=" * 50)
            
            credentials = load_pg_creds()
            full_data = prepare_dataset("dataset.csv", max_rows=100)  
            
            # Меняем базу данных на homeworks в строке подключения
            conn_str = f"postgresql+psycopg2://{credentials['user']}:{credentials['pass']}@{credentials['url']}:{credentials['port']}/homeworks"
            engine = create_engine(conn_str, pool_recycle=3600)
            
            # Загружаем в homeworks
            with engine.begin() as conn:
                full_data.to_sql(
                    name="dolgikh",
                    con=conn,
                    schema="public", 
                    if_exists="replace",
                    index=False,
                    method='multi'
                )
            
            print(" Данные успешно загружены в базу homeworks")
            
            # Финальная проверка
            verify_upload(engine, "dolgikh")
            print("\n Готово ")
    else:
        print("\n Не удалось выполнить тест. Проверьте настройки и попробуйте снова.")
