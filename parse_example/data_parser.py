import requests
import csv

def simple_cocktail_parser():
    # Тут список с сайта популярных коктейлей для парсинга
    cocktail_names = [
        'margarita', 'mojito', 'martini', 'cosmopolitan', 'old fashioned',
        'daiquiri', 'manhattan', 'whiskey sour', 'pina colada', 'bloody mary'
    ]
    
    base_url = "https://www.thecocktaildb.com/api/json/v1/1" # Ссылочка на сайт
    cocktails_data = []
    
    print("Начинаем парсинг коктейлей...")
    
    for name in cocktail_names:
        try:
            # Тут ищем коктейль по названию
            response = requests.get(f"{base_url}/search.php?s={name}")
            data = response.json()
            
            if data['drinks']:
                drink = data['drinks'][0]
                
                # Тут собираем ингредиенты
                ingredients = []
                for i in range(1, 16):
                    ingredient = drink.get(f'strIngredient{i}')
                    if ingredient and ingredient.strip():
                        ingredients.append(ingredient.strip())
                
                # Тут формируем данные коктейля ( состав )
                cocktail = {
                    'id': drink['idDrink'],
                    'name': drink['strDrink'],
                    'category': drink['strCategory'],
                    'glass': drink['strGlass'],
                    'instructions': drink['strInstructions'][:100] + '...' if len(drink['strInstructions']) > 100 else drink['strInstructions'],
                    'ingredients': ', '.join(ingredients),
                    'ingredient_count': len(ingredients)
                }
                
                cocktails_data.append(cocktail)
                print(f"✓ {drink['strDrink']} - {len(ingredients)} ингредиентов")
                
        except Exception as e:
            print(f"✗ Ошибка при парсинге {name}: {e}")
    
    # Сохраняем в CSV
    if cocktails_data:
        with open('cocktails.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=cocktails_data[0].keys())
            writer.writeheader()
            writer.writerows(cocktails_data)
        
        print(f"\n Успешно сохранено {len(cocktails_data)} коктейлей в cocktails.csv")
        
        # Выводим первые 10 строк
        print("\n" + "="*50)
        print("ПЕРВЫЕ 10 КОКТЕЙЛЕЙ:")
        print("="*50)
        
        for i, cocktail in enumerate(cocktails_data[:10], 1):
            print(f"\n{i}. {cocktail['name']}")
            print(f"   Категория: {cocktail['category']}")
            print(f"   Бокал: {cocktail['glass']}")
            print(f"   Ингредиенты: {cocktail['ingredients']}")
            print(f"   Кол-во ингредиентов: {cocktail['ingredient_count']}")
            print(f"   Инструкция: {cocktail['instructions']}")
            print("-" * 40)

# Запускаем парсер
if __name__ == "__main__":
    simple_cocktail_parser()
