numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
operacao = input("Digite uma operação básica: ")

if operacao == "+":
    conta = numero1 + numero2
    print(f"A soma é {conta}")

elif operacao == "-":
    conta = numero1 - numero2
    print(f"A subtração é {conta}")

elif operacao == "*":
    conta = numero1 * numero2
    print(f"A multiplicação é {conta}")

elif operacao == "/":
    conta = numero1 / numero2
    print(f"A divisão é {conta}")