#Criar txt chamado "meu_arquivo.txt" e escrever "Olá, mundo" e "Python é divertido"

with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo: #o w é para write, o r é para read
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Aprendendo Python\n")
    #outros comandos: .with_open() e .read()