temperatura = float(input("Digite a temperatura atual: "))

if temperatura < 10:
    print("Frio")
elif temperatura >= 10 and temperatura <= 25:
    print("Aconchegante")
elif temperatura > 25 and temperatura <= 40:
    print("Quente")
elif temperatura > 40:
    print("Muito quente")