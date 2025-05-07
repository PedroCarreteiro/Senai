def fatorial(n):
    r = 1
    for r in range(1,n):
        n *= r
    return n

try:
    n = int(input("Digite o número inteiro: "))
    print(f"O fatorial de {n} é {fatorial(n)}")
except:
    print("O número digitado não é inteiro!")

