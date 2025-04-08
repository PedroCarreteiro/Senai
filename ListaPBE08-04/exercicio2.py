N = int(input("Digite um número positivo: "))
tamanho = N
soma = 0
i = 0

if N <= 0:
    print("INVALIDO")
else:
    while i != tamanho:
        soma = N+soma
        i+=1
        N-=1

    print(f"A soma é {soma}")