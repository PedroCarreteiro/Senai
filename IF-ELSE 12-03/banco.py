idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda: "))

if idade >= 18 and renda > 1500.00:
    print("Empréstimo autorizado pois você é de maior e tem renda maior que R$1500.00")
elif idade < 18 and renda > 1000.00:
    print("Empréstimo autorizado, mas você é de menor e tem renda maior que R$1000.00")
else:
    print("Empréstimo negado")