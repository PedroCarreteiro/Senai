ano = int(input("Digite o ano: "))

if ano % 4 == 0 and ano % 100 != 0:
    print("Ano bissexto")
elif ano % 400 == 0:
    print("Ano é bissexto")
else:
    print("Ano não bissexto")