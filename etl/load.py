
from pathlib import Path
import sqlite3
import pandas as pd
from sqlalchemy import create_engine, inspect
import os

PROCESSED_DIR = Path.cwd() / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def load_pg_creds(sqlite_path: str = "creds.db"):
    ## читает таблицу access в creds.db
    if not Path(sqlite_path).exists():
        print(f"[load] creds.db не найден по пути: {sqlite_path}")
        return None
    try:
        with sqlite3.connect(sqlite_path) as conn:
            creds = pd.read_sql_query("SELECT url, port, user, pass FROM access LIMIT 1;", conn)
        if creds.empty:
            print("[load] creds.db не содержит записей в таблице access")
            return None
        return creds.iloc[0].to_dict()
    except Exception as e:
        print(f"[load][ERROR] Не удалось прочитать creds.db: {e}")
        return None


def save_parquet(df: pd.DataFrame, name: str = "dataset_processed.parquet") -> Path:
    out = PROCESSED_DIR / name
    df.to_parquet(out, index=False)
    print(f"[load] Сохранён parquet -> {out}")
    return out


def upload_to_postgres(df: pd.DataFrame, creds: dict, table_name: str = "dolgikh", max_rows: int = 100):
    # Обрезаем до max_rows
    df_to_upload = df.head(max_rows).copy()
    # Нормализация имён колонок: lower_snake_case
    df_to_upload.columns = [col.strip().lower().replace(" ", "_") for col in df_to_upload.columns]
    try:
        conn_str = f"postgresql+psycopg2://{creds['user']}:{creds['pass']}@{creds['url']}:{creds['port']}/homeworks"
        print(f"[load] Подключение к Postgres: {creds['url']}:{creds['port']}/homeworks")
        engine = create_engine(conn_str, pool_recycle=3600, connect_args={'connect_timeout': 10})
        # Тест подключения
        with engine.connect() as conn:
            print("[load] Соединение с Postgres успешно.")
        # Запись
        with engine.begin() as conn:
            df_to_upload.to_sql(
                name=table_name,
                con=conn,
                schema="public",
                if_exists="replace",
                index=False,
                method='multi'
            )
        # Проверка
        inspector = inspect(engine)
        tables = inspector.get_table_names(schema="public")
        if table_name in tables:
            print(f"[load] Таблица '{table_name}' успешно загружена в схему public.")
            return engine
        else:
            print(f"[load][WARN] Таблица '{table_name}' не найдена после загрузки. Текущие таблицы: {tables}")
            return engine
    except Exception as e:
        print(f"[load][ERROR] Ошибка при загрузке в Postgres: {e}")
        return None


def load_and_save(df: pd.DataFrame, creds_db_path: str = "creds.db", table_name: str = "dolgikh", max_rows: int = 100):
    # Сначала сохраняем parquet локально
    save_parquet(df, name=f"{table_name}_processed.parquet")
    creds = load_pg_creds(creds_db_path)
    if creds:
        engine = upload_to_postgres(df, creds, table_name=table_name, max_rows=max_rows)
        if engine:
            print("[load] Upload complete.")
            return True
        else:
            print("[load] Upload failed; parquet сохранён локально.")
            return False
    else:
        print("[load] Нет учетных данных; parquet сохранён локально. Для загрузки в Postgres добавьте creds.db.")
        return False


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Путь к очищенному csv (data/raw/...)")
    p.add_argument("--table", default="dolgikh", help="Имя таблицы в Postgres (lowercase)")
    p.add_argument("--max-rows", type=int, default=100, help="Максимум строк для загрузки")
    p.add_argument("--creds-db", default="creds.db", help="Путь к creds.db")
    args = p.parse_args()
    df = pd.read_csv(args.input)
    load_and_save(df, creds_db_path=args.creds_db, table_name=args.table, max_rows=args.max_rows)

