idade = int(input("Digite sua idade: "))

if idade >= 13 and idade <= 59:
    print("Não tem desconto")
elif idade <= 12:
    print("Tem desconto")
elif idade >= 60:
    print("Tem desconto")