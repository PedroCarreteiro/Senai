numero = int(input("Digite um número positivo: "))
i = 0
lista = []

if numero > 0:
    while i < numero:
        i += 1
        lista.append(1/i)
    soma = sum(lista)
    print(f"A soma é {soma:.2f}")
else:
    print("INVALIDO")
