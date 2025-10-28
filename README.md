# Precipitation Data Analysis and Forecasting 

This repository contains a project focused on the analysis of precipitation data and forecasting weather conditions for several years ahead.  
The work was completed as part of the **Data-Engineering-Dataset** course.  
The project is written in **Python**.

---

## 📊 Project Overview
The main objective of this project is to:
- Analyze historical precipitation data  
- Perform preprocessing and transformation of raw data  
- Visualize precipitation patterns  
- Build models for **forecasting weather conditions** over multiple years  

This project demonstrates fundamental data engineering and machine learning practices.

---

## 📂 Dataset
The dataset used in this project can be accessed here:  
[📎 Precipitation dataset (Google Drive)](https://drive.google.com/file/d/1NPjKJoVKQWytdYYEIFn7WQGVL6Tljo_L/view?usp=drive_link)

The dataset is automatically downloaded and processed by the data loader script.

---

## 🚀 Installation & Usage
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Installation+&+Usage)](https://git.io/typing-svg)

Follow these steps to set up the environment and run the project:

### 1. Create and activate a conda environment
```bash
conda create -n my_env python=3.13 pip
conda activate my_env
```

### 2. Install Poetry
```bash
pip install poetry
```

### 3. Create a new Poetry project (if needed)
```bash
poetry new my_project
cd my_project
```

### 4. Add dependencies with Poetry
```bash
pip install pandas gdown jupyterlab matplotlib seaborn plotly statsmodels numpy
```

### 5. Install dependencies
```bash
poetry install --no-root
```

### 6. Run the data loader script
```bash
python data_loader.py
```

## 🔄 Data Processing Features

The `data_loader.py` script performs the following operations:

- **Automatic Download**: Downloads the dataset from Google Drive using the file ID
- **Data Type Conversion**: 
  - Converts date columns (`Date`, `Date1`) to datetime format
  - Converts all numeric columns to float type for consistent processing
- **Data Validation**: Displays the first 10 rows and data types before/after processing
- **CSV Export**: Saves the processed dataset back to CSV format

## 📷 Script Output Example

When running the script `data_loader.py`, the dataset is automatically downloaded from Google Drive, saved locally, and processed with data type conversions.

Example run:

```bash
(my_env) C:\Users\cdolg\my_project> python data_loader.py
```

<img width="1107" height="632" alt="image" src="https://github.com/user-attachments/assets/15fd6e94-4398-42c6-a4fc-9c668683588e" />


The script will output:
- First 10 rows of the dataset
- Data types before processing
- Data types after processing
- Confirmation that the dataset has been updated

---

## 🛠️ Dependencies

Main dependencies required for this project:
- `pandas` - Data manipulation and analysis
- `gdown` - Download files from Google Drive
- `jupyterlab` - Interactive development environment
- `matplotlib` - Data visualization
- `seaborn` - Statistical data visualization
- `statsmodels` - Statistical models and time series decomposition
- `plotly` - Interactive visualizations and dashboards

plotly - Interactive visualizations and dashboards
---

# Precipitation Data Analysis and Forecasting 

This repository contains a project focused on the analysis of precipitation data and forecasting weather conditions for several years ahead.  
The work was completed as part of the **Data-Engineering-Dataset** course.  
The project is written in **Python**.

---

## 📁 Project Structure

---

```

my_project/
│
├── etl/                     # Пакет ETL
│   ├── **init**.py
│   ├── extract.py            # Загрузка и базовая валидация CSV из Google Drive
│   ├── transform.py          # Приведение типов, очистка данных
│   ├── load.py               # Загрузка в PostgreSQL и сохранение parquet
│   ├── validate.py           # Дополнительные проверки данных
│   └── main.py               # CLI интерфейс для запуска ETL
│
├── data/                     # Папка с данными (НЕ пушится в git)
│   ├── raw/                  # Сырые CSV-файлы
│   └── processed/            # Преобразованные parquet-файлы
│
├── creds.db                  # SQLite с учетными данными для PostgreSQL (опционально)
├── README.md
├── requirements.txt
└── .gitignore

````

> ⚠️ Важно: папка `data/` добавлена в `.gitignore` и **не должна попадать в репозиторий**.

---

## 📖 Функции пакета

### 1. Extract (`extract.py`)
- Скачивает CSV-файл из Google Drive (`file_id` или `url`) через `gdown`.
- Базовая валидация: проверка читаемости CSV, наличия строк.
- Сохраняет исходный CSV в `data/raw/`.

**Пример использования:**
```bash
python -m etl.main extract --file-id <GDRIVE_FILE_ID> --output dataset.csv
````

---

### 2. Transform (`transform.py`)

* Чтение CSV из `data/raw/`.
* Приведение типов: даты → datetime, числовые колонки → float/int.
* Удаление полностью пустых колонок.
* Сохраняет очищенный CSV в `data/raw/`.

**Пример использования:**

```bash
python -m etl.main transform --input data/raw/dataset.csv --output dataset_cleaned.csv
```

---

### 3. Validate (`validate.py`)

* Проверяет:

  * нет полностью пустых колонок
  * обязательные колонки присутствуют
  * датафрейм не пустой
* Вызов встроен в пайплайн перед загрузкой.

---

### 4. Load (`load.py`)

* Чтение `creds.db` (SQLite) для получения учетных данных PostgreSQL.
* Загрузка до 100 строк в базу `homeworks`, схема `public`.
* Сохраняет результат в parquet: `data/processed/<table_name>_processed.parquet`.
* Если Postgres недоступен — сохраняет parquet локально.

**Пример использования:**

```bash
python -m etl.main load --input data/raw/dataset_cleaned.csv --table dolgikh --max-rows 100 --creds-db creds.db
```

---

### 5. Main CLI (`main.py`)

* Объединяет весь пайплайн: **extract → transform → validate → load**.
* Минимальный обязательный аргумент: команда `run`, `extract`, `transform` или `load`.
* Для команды `run` обязательно указывать `--file-id`.

**Пример полного запуска:**

```bash
python -m etl.main run --file-id 1NPjKJoVKQWytdYYEIFn7WQGVL6Tljo_L
```

**Пример с кастомными настройками:**

```bash
python -m etl.main run \
    --file-id 1NPjKJoVKQWytdYYEIFn7WQGVL6Tljo_L \
    --output dataset.csv \
    --cleaned-name dataset_cleaned.csv \
    --table dolgikh \
    --max-rows 100 \
    --creds-db creds.db
```

---

## 💡 Требования

* Python >= 3.9
* Библиотеки:

```bash
pip install -r requirements.txt
```

Список зависимостей в `requirements.txt`:

```
pandas
gdown
sqlalchemy
psycopg2-binary
pyarrow
```

> ⚠️ Для сохранения в `.parquet` обязательно нужен `pyarrow` или `fastparquet`.

---

## ⚙️ Настройка

1. Поместите `creds.db` в корень проекта (если требуется загрузка в PostgreSQL).
   Таблица `access` должна содержать колонки: `url`, `port`, `user`, `pass`.
2. Убедитесь, что каталоги `data/raw/` и `data/processed/` существуют (скрипт создаст их автоматически при запуске).
3. Настройте `.gitignore`:

```
/data/
__pycache__/
*.pyc
*.pyo
venv/
env/
.my_env/
.vscode/
.idea/
```

---

## 📌 Проверка работы

1. Скачайте CSV через extract.
2. Приведите типы через transform.
3. Валидация пройдена автоматически.
4. Загрузите в PostgreSQL и сохраните parquet через load или run.

**Пример вывода успешного выполнения:**

```
[main] START full run
[extract] CSV прочитан: shape=(3902, 23)
[transform] Сохранён очищенный CSV -> data/raw/dataset_cleaned.csv
[validate] Валидация пройдена: shape=(3902, 23)
[load] Сохранён parquet -> data/processed/dolgikh_processed.parquet
[load] Таблица 'dolgikh' успешно загружена в схему public.
[main] FULL RUN complete.
```

---

## ✅ Замечания

* Таблица в PostgreSQL создаётся с именем из аргумента `--table` (по умолчанию `dolgikh`).
* Если `creds.db` отсутствует — данные сохраняются только в parquet.
* Старые скрипты `data_loader.py` и `write_to_db.py` **не используются и должны быть удалены**.

```

---






