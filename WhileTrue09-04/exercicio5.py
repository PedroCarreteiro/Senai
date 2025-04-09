senha = "senha"
tentativa = 0

while tentativa != 3:
    tentativa += 1
    senha_tentativa = input("Digite sua tentativa da senha: ")
    if senha_tentativa == senha:
        print("Você acertou a senha!")
        break
    if tentativa == 3:
        print("Você esgotou suas tentativas!")
    else:
        print("Senha incorreta! Tente novamente!")
