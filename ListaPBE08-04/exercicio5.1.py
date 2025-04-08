numero = int(input("Digite um número: "))
i = 2
teste = 0
primo = True

if numero > 0:
    while i < numero:
        i += 1
        teste = i
        if numero == teste:
            teste -= 1
            if numero % teste == 0:
                primo = False
            else:
                primo = True
        else:
            if numero % teste == 0:
                primo = False
            else:
                primo = True
    if primo == False:
        print(f"O número {numero} não é primo!")
    else:
        print(f"O número {numero} é primo!")



# if (numero % 1 == 0) and (numero % numero == 0):
#     print(f"O número {numero} é primo!")