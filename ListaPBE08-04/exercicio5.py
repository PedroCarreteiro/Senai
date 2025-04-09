numero = int(input("Digite um número positivo: "))
if numero > 1:
    for i in range(2, numero): #testar números do 2 até o número - 1
        if numero % i == 0:
            print(f"O número {numero} não é primo.")
            break
    else:
        print(f"O número {numero} é primo.")
else:
    print("INVALIDO")