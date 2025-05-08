def contagem_regressiva(n):
    if n < 1:
        print("Fim")
    else:
        print(n)
        contagem_regressiva(n - 1)

n = int(input("Digite um número: "))

contagem_regressiva(n)
