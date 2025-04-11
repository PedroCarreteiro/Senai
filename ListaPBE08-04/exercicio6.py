numeros = int(input("Quantos numeros você quer: "))

a = 0 #primeiro numero
b = 1 #segundo numero
i = 0
sequencia = ""

if numeros > 0:

    while i < numeros: #enquanto contador for menor que a quantidade de numeros
        sequencia += str(a)
        if i < numeros - 1: #se não é o último termo (o if com o -1 é para não imprimir a vírgula)
            sequencia += ", "
        a, b = b, a + b #substituir a por b e b por a + b
        i += 1

    print(sequencia)

else:
    print("INVALIDO")
