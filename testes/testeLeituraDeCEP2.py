import pandas as pd
import pycep_correios as pycep

low_memory = False
pd.options.display.max_rows = 100

ceps = pd.read_excel('CNES_01_04_2020_banco_estab.xlsx', usecols = 'I')
