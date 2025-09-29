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
poetry add jupyterlab pandas matplotlib gdown
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

---

## 📁 Project Structure

```
my_project/
├── data_loader.py          # Main data loading and processing script
├── dataset.csv            # Processed dataset (generated)
├── pyproject.toml         # Poetry configuration
└── README.md              # Project documentation
```
## 📷 Script Output Example

When running the script `data_loader.py`, the dataset is automatically downloaded from Google Drive, saved locally, and the first 10 rows are displayed in the console.

Example run:

```bash
(my_env) C:\Users\cdolg\my_project> python data_loader.py
```
<img width="1107" height="632" alt="image" src="https://github.com/user-attachments/assets/15fd6e94-4398-42c6-a4fc-9c668683588e" />


