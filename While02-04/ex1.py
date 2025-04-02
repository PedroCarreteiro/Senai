numero = int(input("Digite um número de 5 a 10: "))

if numero >= 5 and numero <=10:
    while numero >= 0:
        print(numero)
        numero -= 1
else:
    print("O número digitado não está entre 5 e 10.")