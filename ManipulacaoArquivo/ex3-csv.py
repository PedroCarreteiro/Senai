#comandos csv
#.biblioteca csv
#.with.open()
#.writer()
#.writerow()
#.reader

import csv

with open("produtos.csv", "w", encoding="utf-8", newline='') as arquivo: #o w é para write, o r é para read
    arquivo_writer = csv.writer(arquivo)

    arquivo_writer.writerow(["Nome","Preço"])
    arquivo_writer.writerow(["Livro",20])

with open("produtos.csv", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())

