while True:
    print("Bem vindo ao meu menu: \n"
          "Menu \n"
          "Menu também \n"
          "Adivinha? Menu TAMBÉM \n"
          "Sair")
    opcao = input("Digite a opção que você quer: ")
    if opcao.lower() == "sair":
        print("Vcoê saiu do menu!")
        break
    else:
        print("Você continua no menu!")