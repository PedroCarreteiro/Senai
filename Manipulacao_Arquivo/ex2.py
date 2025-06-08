import pandas as pd

df = pd.read_excel('pedidos.xlsx')
df.to_csv('pedidos.csv', index=False)
