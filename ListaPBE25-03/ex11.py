peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso/(altura**2)
classificao = ""

if imc < 18.5:
    classificacao = "Baixo peso"
    print(f"Seu IMC é {imc:.2f} e sua classificação é {classificacao}")
elif imc >= 18.5 and imc <= 24.9:
    classificacao = "Normal"
    print(f"Seu IMC é {imc:.2f} e sua classificação é {classificacao}")
elif imc >= 25 and imc <= 29.9:
    classificacao = "Sobrepeso"
    print(f"Seu IMC é {imc:.2f} e sua classificação é {classificacao}")
elif imc >= 30:
    classificacao = "Obesidade"
    print(f"Seu IMC é {imc:.2f} e sua classificação é {classificacao}")