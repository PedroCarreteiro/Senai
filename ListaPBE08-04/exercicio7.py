i = 0
numero = int(input("Digite a quantidade de itens total: "))

if numero > 0:
    while i <= numero:
        print(f"{"*"*i}")
        i += 1
else:
    print("INVALIDO")