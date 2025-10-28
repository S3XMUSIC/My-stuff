# Precipitation Data Analysis and Forecasting 

This repository contains a project focused on the analysis of precipitation data and forecasting weather conditions for several years ahead.  
The work was completed as part of the **Data-Engineering-Dataset** course.  
The project is written in **Python**.

---

## 📊 Project Overview
The main objectives of the project:
- Analysis of historical precipitation data
- Preprocessing and transformation of raw data
- Visualization of precipitation patterns
- Building models for **weather forecasting** for several years ahead

The project demonstrates fundamental data engineering and machine learning practices.

---

## 📂 Dataset
The dataset used is available at:  
[📎 Precipitation dataset (Google Drive)](https://drive.google.com/file/d/1NPjKJoVKQWytdYYEIFn7WQGVL6Tljo_L/view?usp=drive_link)

The dataset is automatically downloaded and processed by the ETL pipeline.

---

## 🏗️ Project Structure

```
project/
├── etl/                    # ETL pipeline
│   ├── __init__.py
│   ├── extract.py         # Data loading from Google Drive
│   ├── transform.py       # Data transformation and cleaning
│   ├── load.py            # Loading to DB and export to parquet
│   ├── validate.py        # Data validation
│   └── main.py            # CLI entry point
├── EDA.ipynb              # Exploratory Data Analysis
├── notebooks/             # Additional notebooks
├── data/                  # Data (auto-created)
│   ├── raw/              # Raw data
│   └── processed/        # Processed data
├── requirements.txt       # Dependencies
└── README.md
```

---

## 🚀 Installation and Usage

### 1. Create and activate conda environment
```bash
conda create -n my_env python=3.13 pip
conda activate my_env
```

### 2. Install Poetry
```bash
pip install poetry
```

### 3. Install dependencies
```bash
poetry install --no-root
```

Or direct installation:
```bash
pip install pandas gdown jupyterlab matplotlib seaborn plotly statsmodels numpy sqlalchemy psycopg2-binary pyarrow
```

---

## 🔄 ETL Pipeline

The project includes a reusable **ETL package** for processing precipitation data:

### Running the full pipeline

```bash
python -m etl.main run --file-id 1NPjKJoVKQWytdYYEIFn7WQGVL6Tljo_L
```

* `--file-id` — Google Drive file ID

### Running individual stages

```bash
# Data extraction only
python -m etl.main extract --file-id 1NPjKJoVKQWytdYYEIFn7WQGVL6Tljo_L

# Data transformation only
python -m etl.main transform --input data/raw/dataset.csv

# Data loading only
python -m etl.main load --input data/processed/dataset_cleaned.csv --table precipitation_data
```

### ETL Functionality

- **Extract**: Automatic dataset download from Google Drive
- **Transform**: 
  - Conversion of date columns (`Date`, `Date1`) to datetime format
  - Conversion of numeric columns to float for consistency
  - Data validation
- **Load**: Saving up to 100 rows to PostgreSQL and export to Parquet

---

## 📊 Exploratory Data Analysis (EDA)


Run the notebook for data analysis:

```bash
jupyter notebook EDA.ipynb
```

The `EDA.ipynb` notebook contains:
- Precipitation distribution visualization
- Time series analysis
- Statistical summaries
- Pattern and anomaly detection

---

## 📷 Example Output

When running the ETL pipeline, the output includes:

```bash
(precipitation_env) C:\Users\cdolg\my_project> python -m etl.main run --file-id 1NPjKJoVKQWytdYYEIFn7WQGVL6Tljo_L --table precipitation_data

[INFO] Starting ETL pipeline...
[INFO] Data downloaded successfully: data/raw/dataset.csv
[INFO] Data transformed successfully
[INFO] First 10 rows of processed data:
...
[INFO] Data types before and after transformation:
...
[INFO] 100 rows loaded to PostgreSQL table: precipitation_data
[INFO] Data exported to parquet: data/processed/dataset_cleaned.parquet
```

---

## 🛠️ Dependencies

Main project dependencies:
- `pandas` - Data manipulation and analysis
- `gdown` - Download files from Google Drive
- `jupyterlab` - Interactive development environment
- `matplotlib`, `seaborn`, `plotly` - Data visualization
- `statsmodels` - Statistical models and time series decomposition
- `sqlalchemy`, `psycopg2-binary` - PostgreSQL integration
- `pyarrow` - Parquet format export
- `numpy` - Scientific computing
