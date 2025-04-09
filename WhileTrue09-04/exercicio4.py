numero1 = int(input("Digite o número inicial: (ele dever ser positivo): "))
numero2 = int(input("Digite o número final: (ele dever ser positivo): "))
primo = True

if numero1 < numero2:
    for n in range(numero1+1, numero2):
        i = 2 #divisor
        while i < n:
            if n % i == 0 or n == 1:
                primo = False
                break
            else:
                primo = True
                i+=1

        if primo:
            print(n)

else:
    print("Números inválidos")

