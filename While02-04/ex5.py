operacao = "";
op = "";

while op != "sair":
    operacao = input("Digite uma operação (+ - / *)(se quiser sair, digite 'sair'): ")
    op = operacao.lower()
    if operacao == "sair" or operacao == "+" or operacao == "*" or operacao == "/" or operacao == "-":
        if op != "sair":
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            if op == "+":
                conta = numero1 + numero2
                print(f"A soma entre {numero1} e {numero2} é {conta}.")
            elif op == "-":
                conta = numero1 - numero2
                print(f"A subtração entre {numero1} e {numero2} é {conta}.")
            elif op == "/":
                conta = numero1 / numero2
                print(f"A divisão entre {numero1} e {numero2} é {conta}.")
            elif op == "*":
                conta = numero1 * numero2
                print(f"A multiplicação entre {numero1} e {numero2} é {conta}.")
        else:
            print("Você saiu do programa!")
    else:
        print("Operação inválida!")