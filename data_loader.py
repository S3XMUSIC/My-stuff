import gdown  # специально для Gdrive
import pandas as pd

FILE_ID = "1NPjKJoVKQWytdYYEIFn7WQGVL6Tljo_L"  # Тут вставляет ваш ID документа из гугл диска, если собственный дата сет
URL = f"https://drive.google.com/uc?id={FILE_ID}"

OUTPUT = "dataset.csv"  # Тут качаем файл
gdown.download(URL, OUTPUT, quiet=False)

df = pd.read_csv(OUTPUT)

print(df.head(10))  # Тут выводим первые 10 значений из датасета для проверки читаемости

df = pd.read_csv("dataset.csv")  # Тут читаем данные

print("Типы до обработки:")
print(df.dtypes)

df["Date"] = pd.to_datetime(df["Date"])  # Преобразую даты в тип дата
df["Date1"] = pd.to_datetime(df["Date1"])

numeric_columns = [
    "Average temperature (°F)",
    "Average humidity (%)",
    "Average dewpoint (°F)",
    "Average barometer (in)",
    "Average windspeed (mph)",
    "Average gustspeed (mph)",
    "Average direction (°deg)",
    "Rainfall for month (in)",
    "Rainfall for year (in)",
    "Maximum rain per minute",
    "Maximum temperature (°F)",
    "Minimum temperature (°F)",  # Список числовых столбцов
    "Maximum humidity (%)",
    "Minimum humidity (%)",
    "Maximum pressure",
    "Minimum pressure",
    "Maximum windspeed (mph)",
    "Maximum gust speed (mph)",
    "Maximum heat index (°F)",
    "Month",
    "diff_pressure",
]

df[numeric_columns] = df[numeric_columns].astype(
    float
)  # Преобразую все числовые столбцы в тип Float

print("\nТипы после обработки:")  # Показываю типы после обработки
print(df.dtypes)

df.to_csv("dataset.csv", index=False)
print("Датасет обновлен в CSV")
