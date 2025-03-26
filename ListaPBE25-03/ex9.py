valor = float(input("Digite o valor da compra: "))
desconto = 0

if valor < 100:
    desconto = (valor/100) * 5
    valor_com_desconto = valor-desconto
    print(f"O valor com desconto é: {valor_com_desconto}")
elif valor >= 100 and valor <= 500:
    desconto = (valor/100) * 10
    valor_com_desconto = valor-desconto
    print(f"O valor com desconto é: {valor_com_desconto}")
elif valor > 500:
    desconto = (valor/100) * 15
    valor_com_desconto = valor-desconto
    print(f"O valor com desconto é: {valor_com_desconto}")