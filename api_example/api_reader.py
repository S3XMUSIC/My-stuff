import requests
import pandas as pd
import json

def fetch_cocktails_by_first_letter(letter='a'):
    """
    Функция для получения коктейлей по первой букве названия
    """
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

def process_cocktail_data(api_data):
    """
    Функция для обработки данных и создания DataFrame
    """
    if not api_data or 'drinks' not in api_data or api_data['drinks'] is None:
        print("Нет данных о коктейлях")
        return pd.DataFrame()
    
    cocktails = []
    
    for drink in api_data['drinks']:
        # Тут собираем ингредиенты и их количество
        ingredients = []
        measures = []
        
        for i in range(1, 16):  # API предоставляет до 15 ингредиентов
            ingredient = drink.get(f'strIngredient{i}')
            measure = drink.get(f'strMeasure{i}')
            
            if ingredient and ingredient.strip():
                ingredients.append(ingredient.strip())
                measures.append(measure.strip() if measure else 'По вкусу')
        
        # Тут создаем запись для коктейля
        cocktail_data = {
            'id': drink['idDrink'],
            'name': drink['strDrink'],
            'category': drink['strCategory'],
            'alcoholic': drink['strAlcoholic'],
            'glass': drink['strGlass'],
            'instructions': drink['strInstructions'],
            'ingredients': ', '.join(ingredients),
            'measures': ', '.join(measures),
            'image_url': drink['strDrinkThumb']
        }
        
        cocktails.append(cocktail_data)
    
    return pd.DataFrame(cocktails)

def main():
    """
    Основная функция для выполнения задания
    """
    print("Загрузка данных из The CocktailDB API...")
    
    # Получаем данные из API
    api_data = fetch_cocktails_by_first_letter('a')
    
    if api_data:
        # Создаем DataFrame
        df = process_cocktail_data(api_data)
        
        if not df.empty:
            # Выводим информацию о DataFrame
            print(f"\nУспешно загружено {len(df)} коктейлей")
            print(f"Размер DataFrame: {df.shape}")
            print("\nПервые 5 записей:")
            print(df.head())
            
            # Базовая информация о данных
            print("\nИнформация о DataFrame:")
            print(df.info())
            
            # Сохраняем в CSV файл (опционально)
            df.to_csv('cocktails_data.csv', index=False, encoding='utf-8')
            print(f"\nДанные сохранены в файл: cocktails_data.csv")
            
            # Дополнительный анализ
            print("\nСтатистика по категориям:")
            print(df['category'].value_counts())
            
            print("\nСтатистика по типам напитков:")
            print(df['alcoholic'].value_counts())
            
        else:
            print("Не удалось создать DataFrame")
    else:
        print("Не удалось получить данные из API")

# Альтернативная версия - загрузка коктейлей по названию
def fetch_cocktail_by_name(name):
    """
    Функция для поиска конкретного коктейля по названию
    """
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

def example_with_margarita():
    """
    Пример с загрузкой данных о маргарите (как в вашем первом примере)
    """
    print("\n" + "="*50)
    print("Пример с загрузкой данных о Маргарите")
    print("="*50)
    
    api_data = fetch_cocktail_by_name('margarita')
    
    if api_data and 'drinks' in api_data:
        df_margarita = process_cocktail_data(api_data)
        
        if not df_margarita.empty:
            print(f"Найдено {len(df_margarita)} вариантов маргариты:")
            for idx, row in df_margarita.iterrows():
                print(f"{idx+1}. {row['name']} - {row['category']}")

if __name__ == "__main__":
    main()
    example_with_margarita()
