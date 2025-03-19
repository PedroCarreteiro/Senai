import random

chute = input("Escolha P para Pedra, A para Papel e T para tesoura: ").upper()
opcoes = ["P","A","T"]

escolha = random.choice(opcoes)

if chute == "P" or "A" or "T":
    if chute == escolha:
        print("Empate")
        print(f"A escolha do computador é {escolha}")
    elif chute == "P" and escolha == "A":
        print("Você perdeu")
        print(f"A escolha do computador é {escolha}")
    elif chute == "P" and escolha == "T":
        print("Você ganhou!")
        print(f"A escolha do computador é {escolha}")
    elif chute == "A" and escolha == "T":
        print("Você perdeu")
        print(f"A escolha do computador é {escolha}")
    elif chute == "T" and escolha == "P":
        print("Você perdeu")
        print(f"A escolha do computador é {escolha}")
    elif chute == "T" and escolha == "A":
        print("Você ganhou")
        print(f"A escolha do computador é {escolha}")
else:
    print("Opção inválida")