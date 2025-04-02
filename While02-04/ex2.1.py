maior = 0
contador = 1

while contador <= 5:
    numero = float(input("Digite um número: "))
    if numero > maior:
        maior = numero
    contador += 1
print("O maior número é: ",maior)