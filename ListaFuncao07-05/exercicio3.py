def converter_celsius_fahrenheit(c):
    conversao_temperatura = (c * 9 / 5) + 32
    return conversao_temperatura

temperatura = float(input("Digite a temperatura em celsius: "))

print(f"A temperatura em Fahrenheit é: {converter_celsius_fahrenheit(temperatura)}")