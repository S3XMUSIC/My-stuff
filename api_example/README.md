```markdown
Cocktail API Data Fetcher 🍸

A script for fetching and analyzing cocktail data from The CocktailDB API.

Description

This project provides tools for:
- Fetching cocktail data by the first letter of their name
- Searching for specific cocktails by name
- Processing and analyzing data using pandas
- Saving results to CSV files

Installation and Environment Setup

1. Creating Virtual Environment with Conda

```bash
Create a new environment with Python 3.9
conda create -n cocktail-env python=3.9

Activate the environment
conda activate cocktail-env
```

### 2. Installing Dependencies

```bash
# Install packages from conda
conda install pandas requests

# Or use pip for installation
pip install pandas requests
```

### 3. Verification

```bash
python -c "import pandas, requests; print('All packages installed successfully!')"
```

## Usage

### Basic Functionality

```python
# Run the main script
python cocktail_api.py

# Or use in your own code
from cocktail_api import fetch_cocktails_by_first_letter, process_cocktail_data

# Get cocktails starting with 'a'
data = fetch_cocktails_by_first_letter('a')
df = process_cocktail_data(data)
```

### Available Functions

- `fetch_cocktails_by_first_letter(letter)` - cocktails by first letter
- `fetch_cocktail_by_name(name)` - search cocktail by name
- `process_cocktail_data(api_data)` - process data into DataFrame

## Usage Examples

### Get Cocktails by Letter

```python
from cocktail_api import fetch_cocktails_by_first_letter, process_cocktail_data

# Get cocktails starting with 'b'
data = fetch_cocktails_by_first_letter('b')
cocktails_df = process_cocktail_data(data)

print(f"Found {len(cocktails_df)} cocktails")
print(cocktails_df.head())
```

### Search Specific Cocktail

```python
from cocktail_api import fetch_cocktail_by_name

# Search for margarita
margarita_data = fetch_cocktail_by_name('margarita')
```

## Data Structure

The resulting DataFrame contains the following columns:
- `id` - unique cocktail identifier
- `name` - cocktail name
- `category` - category
- `alcoholic` - alcoholic/non-alcoholic
- `glass` - glass type
- `instructions` - preparation instructions
- `ingredients` - list of ingredients
- `measures` - ingredient measures
- `image_url` - image URL

## Output

The script creates a CSV file `cocktails_data.csv` with the fetched data and outputs to console:
- Statistics of loaded data
- Category distribution
- Drink types (alcoholic/non-alcoholic)

## Requirements

- Python 3.7+
- pandas
- requests

## Deactivating Environment

```bash
# When finished working
conda deactivate

# To remove environment (optional)
conda remove -n cocktail-env --all
```

## Notes

- API has request rate limits
- Data is provided in English
- Internet connection required

---

**Enjoy exploring the world of cocktails!** 🍹
```
