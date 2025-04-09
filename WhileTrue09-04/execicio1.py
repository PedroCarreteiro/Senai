i = 0
lista_jafoi = []
lista_resultado = []

for i in range(10):
    numero = int(input("Digite um número: "))
    if numero % 3 == 0 and numero not in lista_jafoi:
        lista_resultado.append(numero)
    lista_jafoi.append(numero)

quantidade = len(lista_resultado)

print(f"A quantidade de números digitados divisíveis por 3 é: {quantidade}")