numero = 0
lista_numeros = []

for numero in range(1, 10000):
    lista_contador = []

    for i in range(1, numero):
        if numero % i == 0:
            lista_contador.append(i)

    soma = sum(lista_contador)
    if soma == numero:
        lista_numeros.append(numero)

print(f"A lista de números perfeitos de 1 até 10000 é {lista_numeros}")
