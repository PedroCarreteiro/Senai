lista_tamanho = int(input("Dgite o tamanho da lista: "))
lista = []

for i in range(lista_tamanho):
    i += 1
    numero = float(input(f"Digite o número {i}: "))
    lista.insert(1, numero)
    soma = sum(lista)
    media = soma / lista_tamanho

print(media)