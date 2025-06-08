import pandas as pd

df = pd.read_csv('pedidos.csv')
df.to_json('pedidos.json', orient='records', force_ascii=False) #orientar em records para cada linha ser um dicionário diferente e o force ASCII é para preservar acentos
