operacao = input("Qual a medida da temperatura atual? (Digite C para Celsius ou F para Fahrenheit): ").upper()
temperatura = float(input("Digite a temperatura atual: "))

if operacao == "C":
    calculo = temperatura * 1.8 + 32
    print(f"A temperatura em Fahrenheit é {calculo}")
elif operacao == "F":
    calculo = (temperatura-32)/1.8
    print(f"A teperatura em Celsius é {calculo}")
else:
    print("Operação inválida")