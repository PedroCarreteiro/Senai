import pandas as pd #importar biblioteca

csv = pd.read_csv('LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv') #ler csv com o pf.read_csv

csv.to_excel("Excel.xlsx",sheet_name="Esteira",index=True) #converter o csv para um arquivo excel com índice