numero = int(input("Digite um número positivo: "))
lista = []

if numero > 0:
    for i in range(1, numero):
        if numero % i == 0:
            lista.append(i)
    soma = sum(lista)
    if soma == numero:
        print("O número é perfeito!")
    else:
     print("O número não é perfeito!")
else:
    print("INVALIDO")