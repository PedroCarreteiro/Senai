numero = int(input("Digite um número: "))
fatorial = 1
i = 1
while i <= numero:
    fatorial *= i
    i+=1
print(f"O fatorial de {numero} é {fatorial}")