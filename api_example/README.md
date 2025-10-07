
# Cocktail Explorer API 🍸

A sleek Python wrapper for The CocktailDB API with data processing capabilities.

## Quick Start

### 1. Create Environment
```bash
conda create -n cocktail-api python=3.9 pandas requests
conda activate cocktail-api
```

### 2. Run the Script
```bash
python api_reader.py
```

## Features

- 🔍 **Search cocktails** by name or first letter
- 📊 **Auto-convert** API data to pandas DataFrame
- 💾 **Export results** to CSV
- 🎯 **Smart processing** of ingredients and measurements

## Basic Usage

```python
from cocktail_api import fetch_cocktails_by_first_letter

# Get cocktails starting with 'a'
data = fetch_cocktails_by_first_letter('a')
```

## Example Output
```
✅ Successfully loaded 25 cocktails
📊 DataFrame size: (25, 9)
📁 Saved to: cocktails_data.csv
```

## API Functions

| Function | Purpose |
|----------|---------|
| `fetch_cocktails_by_first_letter()` | Cocktails by letter |
| `fetch_cocktail_by_name()` | Search by name |
| `process_cocktail_data()` | Convert to DataFrame |

## Data Columns
- `name`, `category`, `alcoholic`, `glass`
- `ingredients`, `measures`, `instructions`
- `image_url`, `id`

## Requirements
- Python 3.7+
- pandas, requests
- 
Example run:

```bash
(second_my_env) C:\Users\cdolg\api> python api_reader.py
```

<img width="1458" height="588" alt="image" src="https://github.com/user-attachments/assets/3a08034a-fcb9-4502-9c35-3d226360d9a0" />
<img width="1463" height="700" alt="image" src="https://github.com/user-attachments/assets/c5b31c03-9c71-46ae-b51b-47e45dca8d39" />
<img width="1456" height="376" alt="image" src="https://github.com/user-attachments/assets/a3547ff2-40b3-41f6-9885-98cf7aa65df8" />


