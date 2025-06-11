lista = []
lista_ordenada = []

for i in range(10):
    n = int(input("Digite um número para a lista: "))
    lista.append(n)

for i in range(10):
    n = int(input("Digite um número para a lista: "))
    lista_ordenada.append(n)

lista_ordenada = set(lista_ordenada)
lista_ordenada = list(lista_ordenada)
lista_ordenada = sorted(lista_ordenada)

print(lista)
print(lista_ordenada)
