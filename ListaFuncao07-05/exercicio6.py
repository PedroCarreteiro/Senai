def contar_vogais(palavra):
    contador = 0
    palavra = list(palavra)
    print(palavra)
    for i in range(len(palavra)):
        if palavra[i] == "a":
            contador += 1
    return contador

palavra = input("Digite uma palavra: ")

print(f"Essa palavra tem: {contar_vogais(palavra)} vogais")