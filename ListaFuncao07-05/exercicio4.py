def calcular_troco(valor_compra,valor_pago):
    if valor_pago > valor_compra:
        print(f"O valor do troco é: {valor_pago-valor_compra}")
    elif valor_compra > valor_pago:
        print("Pagamento insuficiente!")
        return 0
    else:
        print("O valor está exato, tenha um ótimo dia!")

valor_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor pago: "))

calcular_troco(valor_compra,valor_pago)
