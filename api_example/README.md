
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
python cocktail_api.py
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

