senha = "senha"

while True:
    senha_tentativa = input("Digite sua tentativa da senha: ")
    if senha_tentativa == senha:
        print("Você acertou a senha!")
        break
    else:
        print("Senha incorreta! Tente novamente!")