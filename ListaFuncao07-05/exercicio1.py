def calculadoraIMC(peso,altura):
    imc = peso/altura**2
    return imc

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilos: "))

resultado = calculadoraIMC(peso,altura)

print(f"O seu IMC é {resultado:.2f}")