def contar_vogais(palavra):
    contador = 0
    palavra = palavra.lower()
    palavra = list(palavra)
    for i in range(len(palavra)):
        if palavra[i] == "a" or palavra[i] == "e" or palavra[i] == "i" or palavra[i] == "o" or palavra[i] == "u":
            contador += 1
    return contador

palavra = input("Digite uma palavra: ")

print(f"A palavra {palavra} tem: {contar_vogais(palavra)} vogais")
