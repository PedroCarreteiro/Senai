numero = int(input("Digite um número: "))

par = numero % 2
divisivel3 = numero % 3
divisivel5 = numero % 5

if par == 0:
    print("É par")
else:
    print("Não é par")

if divisivel3 == 0:
    print("É divisível por 3")
else:
    print("Não é divisível por 3")

if divisivel5 == 0:
    print("É divisível por 5")
else:
    print("Não é divisível por 5")

