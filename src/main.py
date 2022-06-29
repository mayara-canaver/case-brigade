import pandas as pd
from src import pega_caminho


data_2016 = pd.read_csv(pega_caminho("2016.csv"))

data_2016.head()
