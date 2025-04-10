lista_tamanho = int(input("Digite o tamanho da lista: "))
lista = []
maior = ""

for i in range(lista_tamanho):
    i += 1
    numero = float(input(f"Digite o número {i}: "))
    lista.insert(1, numero)

lista.remove(max(lista)) #genialidade

maior = max(lista)

print(f"O maior é {maior}")