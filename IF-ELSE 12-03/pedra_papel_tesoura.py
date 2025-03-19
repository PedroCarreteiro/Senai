import random

chute = input("Escolha P para Pedra, A para Papel e T para tesoura: ").upper()
opcoes = ["P","A","T"]

escolha = random.choice(opcoes)

if chute == "P" or "A" or "T":
    if chute == escolha:
        print("Empate")
    elif chute == "P" and escolha == "A":
        print("Você perdeu")
    elif chute == "P" and escolha == "T":
        print("Você ganhou!")
    elif chute == "A" and escolha == "T":
        print("Você perdeu")
    elif chute == "T" and escolha == "P":
        print("Você perdeu")
    elif chute == "T" and escolha == "A":
        print("Você ganhou")
else:
    print("Opção inválida")