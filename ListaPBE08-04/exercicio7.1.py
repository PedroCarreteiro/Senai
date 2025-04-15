i = 0
numero = int(input("Digite a quantidade de itens total: "))

if numero >= 0:
    while i <= numero:
        asterisco_unidade = "*"
        asterisco = asterisco_unidade * i
        print(f"{asterisco}")
        i += 1
else:
    print("INVALIDO")
