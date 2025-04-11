numero = 0
lista_numeros = []

for numero in range(1, 10000): #for para numero de 1 até 10000
    lista_contador = [] #zerar a lista de contador

    for i in range(1, numero): #for para contador de 1 até numero
        if numero % i == 0: #se numero / contador der resto 0
            lista_contador.append(i) #adicione contador na lista de contador

    soma = sum(lista_contador) #somar lista de contador
    if soma == numero: #se a soma de todos os divisores de numero for igual ao numero
        lista_numeros.append(numero) #adicionar numero na lista de perfeitos

print(f"A lista de números perfeitos de 1 até 10000 é {lista_numeros}")
