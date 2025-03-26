nome_arquivo = "C:/Users/49300445880/PycharmProjects/PythonProject/Repeticao26-03/arquivo.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip()) #strip é para tirar o espaços do meio e do final, e não entre palavras