lista_tamanho = int(input("Digite o tamanho da lista: "))
lista = []
i=0

while i < lista_tamanho:
    i += 1
    numero = float(input(f"Digite o número {i}: "))
    lista.insert(1, numero)
    soma = sum(lista)
    media = soma / lista_tamanho

print(media)