def media(lista,lista_tamanho):
    soma = sum(lista)
    media = soma / lista_tamanho
    return media

lista_tamanho = int(input("Dgite o tamanho da lista: "))
lista = []

for i in range(lista_tamanho):
    i += 1
    numero = float(input(f"Digite o número {i}: "))
    lista.insert(1, numero)

print(f"A média de números da lista é {media(lista,lista_tamanho)}")