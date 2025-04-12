import math
from os import remove

numero_inicio = int(input("Digite o número de início: "))
numero_fim = int(input("Digite o número de fim: "))

numero_quadrado = 0
numero_quadrado_esquerda = 0
numero_quadrado_direita = 0
numeros_kaprekar = []

if numero_inicio < 0 or numero_fim < 0:
    print("INVALIDO")
elif numero_inicio > numero_fim:
    print("INVALIDO")
else:
    for numero in range (numero_inicio, numero_fim+1):
        numero_quadrado_string_esquerda = ""
        numero_quadrado_string_direita = ""
        numero_quadrado = int(numero_quadrado)
        numero_quadrado = 0

        numero_quadrado = numero**2
        numero_quadrado = str(numero_quadrado)

        numero_meio = len(numero_quadrado) / 2 #achar o meio da lista
        numero_meio = math.floor(numero_meio) #arredondar para baixo

        numero_quadrado_string_esquerda = numero_quadrado[0 : numero_meio] #pegar a esquerda do numero ao quadrado
        numero_quadrado_string_direita = numero_quadrado[numero_meio : len(numero_quadrado)] #pegar a direita

        if numero_quadrado_string_esquerda != '':
            numero_quadrado_esquerda = int(numero_quadrado_string_esquerda) #caso não seja vazio, transformar esquerda em int
        if numero_quadrado_string_direita != '':
            numero_quadrado_direita = int(numero_quadrado_string_direita) #caso não seja vazio, transformar direita em int

        soma = numero_quadrado_esquerda + numero_quadrado_direita

        if soma == numero:
            numeros_kaprekar.append(numero)

    if 0 in numeros_kaprekar:
        numeros_kaprekar.remove(0)
    print(numeros_kaprekar)
