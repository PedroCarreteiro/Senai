i = 0
lista_jafoi = []
lista_resultado_impar = []
lista_resultado_par = []

for i in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0 and numero not in lista_jafoi:
        lista_resultado_par.append(numero)
    elif  numero % 2 != 0 and numero not in lista_jafoi:
        lista_resultado_impar.append(numero)
    lista_jafoi.append(numero)

print(f"Os número ímpares são: {lista_resultado_impar}\n"
      f"Os números pares são: {lista_resultado_par}")