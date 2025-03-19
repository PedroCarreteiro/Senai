idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 70:
    print("Voto obrigatório!")
elif idade >= 16 and idade < 18:
    print("Voto facultativo!")
elif idade < 16:
    print("Não pode votar!")
elif idade >= 70:
    print("Voto facultativo!")