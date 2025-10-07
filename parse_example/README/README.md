```markdown
# Cocktail Parser 🍸

A simple and efficient Python parser for fetching cocktail data from The CocktailDB API.
```
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

- **Визуальный** - с таблицами и примерами вывода
- **Краткий** - только самая важная информация
