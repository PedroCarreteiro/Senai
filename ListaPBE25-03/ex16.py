import math

numero = int(input("Digite um numero: "))

if numero > 100:
    print("Númro muito grande, reduza para um valor abaixo de 100!")
elif numero < 0:
    print("Não é possível calcular a raiz de um número negativo!")
else:
    raiz = math.sqrt(numero)
    print(f"A raiz de {numero} é {raiz:.2f}")