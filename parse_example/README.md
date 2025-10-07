
# Cocktail Parser 🍸

A simple and efficient Python parser for fetching cocktail data from The CocktailDB API.
[📎 The CocktailDB API](https://www.thecocktaildb.com/)

## Quick Start

### 1. Setup Environment
```bash
conda create -n cocktail-parser python=3.9 requests
conda activate cocktail-parser
```

### 2. Run the Parser
```bash
python data_parser.py
```

## What It Does

- 📥 **Fetches data** for 10 popular cocktails
- 🧪 **Extracts ingredients** and instructions
- 💾 **Saves to CSV** for easy analysis
- 📊 **Displays summary** in console

## Features

- ✅ **Automatic ingredient collection** (up to 15 per cocktail)
- 📝 **Instruction trimming** for clean display
- 🎯 **Error handling** for failed requests
- 📋 **Console preview** of first 10 cocktails

## Output Example

```
✓ Margarita - 6 ingredients
✓ Mojito - 7 ingredients
✓ Martini - 4 ingredients

✅ Successfully saved 10 cocktails to cocktails.csv
```

## Data Structure

| Column | Description |
|--------|-------------|
| `id` | Cocktail ID |
| `name` | Cocktail name |
| `category` | Drink category |
| `glass` | Recommended glass |
| `instructions` | Preparation steps |
| `ingredients` | Comma-separated ingredients |
| `ingredient_count` | Number of ingredients |

## CSV Output

The parser creates `cocktails.csv` with all collected data, ready for:
- Data analysis in Excel/Pandas
- Database import
- Further processing

## Popular Cocktails Parsed

- Margarita 🍋
- Mojito 🌿
- Martini 🍸
- Cosmopolitan 🍊
- Old Fashioned 🥃
- Daiquiri 🍓
- Manhattan 🥃
- Whiskey Sour 🥚
- Piña Colada 🍍
- Bloody Mary 🍅

## Requirements

- Python 3.7+
- requests library

## 📷 Script Output Example

Example run:

```bash
(second_my_env) C:\Users\cdolg\api_project> python data_parser.py
```

<img width="1448" height="565" alt="image" src="https://github.com/user-attachments/assets/18757ed8-db18-45e9-a81d-829807de55f2" />
<img width="1469" height="690" alt="image" src="https://github.com/user-attachments/assets/e1e238a2-351c-4260-b61b-b3f3e7bc08c1" />
<img width="1462" height="683" alt="image" src="https://github.com/user-attachments/assets/dc342637-a2da-41ad-8e4b-dd739d6c44e2" />
<img width="1462" height="184" alt="image" src="https://github.com/user-attachments/assets/ff4669a9-3ba7-4d1e-86ff-828f01bde531" />



