lista_tamanho = int(input("Digite o tamanho da lista: "))
lista = []
lista_menores = []

for i in range(lista_tamanho):
    i += 1
    numero = float(input(f"Digite o número {i}: "))
    lista.insert(1, numero)
soma = sum(lista)
media = soma / lista_tamanho

for n in range(lista_tamanho):
    if lista[n] < media:
        lista_menores.append(lista[n])

print(f"Os números abaixo da média são: {lista_menores}")
