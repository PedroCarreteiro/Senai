numero = int(input("Digite um número: "))
fatorial = 1
i = 1

if numero < 0:
    print("INVALIDO")
else:
    while i <= numero:
        fatorial *= i
        i+=1
    print(f"O fatorial de {numero} é {fatorial}")