

import gdown # специально для Gdrive
import pandas as pd

FILE_ID = "1NPjKJoVKQWytdYYEIFn7WQGVL6Tljo_L" # Тут вставляет ваш ID документа из гугл диска, если собственный дата сет
URL = f"https://drive.google.com/uc?id={FILE_ID}"

OUTPUT = "dataset.csv"  # Тут качаем файл
gdown.download(URL, OUTPUT, quiet=False)

raw_data = pd.read_csv(OUTPUT)

print(raw_data.head(10)) # Тут выводим первые 10 значений из датасета
