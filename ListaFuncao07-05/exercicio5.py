def eh_primo(n):
    ehprimo = True
    if n == 1:
        ehprimo = False
    for i in range(2, n):
        if n % i == 0:
            ehprimo = False
    return ehprimo

n = int(input("Digite um número inteiro: "))

print(f"O número {n} é primo? {eh_primo(n)}")

