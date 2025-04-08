numero = int(input("Digite um número: "))
i = 2
teste = 0
primo = True
lista =  []
divisao_lista = []

if numero > 0:
    while i < numero:
        i+=1
        lista.append(i)
        divisao_lista = [float(a) / i for a in divisao_lista]
        if (numero != 2) or (numero % 2 != 0):
            if  divisao_lista != 0:
                print(f"O número {numero} é primo!")
            else:
                print(f"O número {numero} não é primo!")
        else:
            print(f"O número {numero} não é primo!")





# if (numero % 1 == 0) and (numero % numero == 0):
#     print(f"O número {numero} é primo!")