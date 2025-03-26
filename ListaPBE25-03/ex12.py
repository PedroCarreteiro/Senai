numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2 and numero2 > numero3:
    print("Os números estão em ordem decrescente.")
elif numero1 < numero2 and numero2 < numero3:
    print("Os números estão em ordem crescente.")
elif numero1 == numero2 and numero2 == numero3:
    print("Os números são iguais.")
else:
    print("Os números não estão em nenhuma ordem.")