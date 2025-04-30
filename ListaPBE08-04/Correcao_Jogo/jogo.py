import random

while True:

    opcao = input("Iniciar [1]\n"
                  "Sair [2]\n")

    if opcao == "2":
        break
    elif opcao == "1":
        hp = random.randint(200,1000)
        ataque_jogador = random.randint(1,50)
        ataque_robo = random.randint(1,50)
        defesa_robo = random.randint(1,ataque_jogador-1)
        defesa_jogador = random.randint(1, ataque_robo - 1)

        jogador = {
            "hp": hp,
            "ataque": ataque_jogador,
            "defesa": defesa_jogador
        }

        robo = {
            "hp": hp,
            "ataque": ataque_robo,
            "defesa": defesa_robo
        }

        while jogador['hp'] > 0 and robo['hp']>0:
            print(f"Seu HP: {jogador['hp']}")
            print(f"Seu ataque: {jogador['ataque']}  Sua defesa: {jogador['defesa']}")
            print(f"HP inimigo: {robo['hp']}")

            acao = input("[1] para atacar [2] para curar: ")

            if acao == "1":
                dano = max(0,jogador['ataque']-robo['defesa'])
                robo['hp'] -= dano
                print(f"Você causou {dano} de dano!")
                print(f"O inimigo ficou com {robo['hp']} de vida")
            elif acao == "2":
                cura = 20
                if cura + jogador['hp'] > hp:
                    jogador['hp'] = hp
                else:
                    jogador['hp'] += cura

            if robo['hp'] <= 0:
                print("Você venceu!")
                break

            acao = random.choice(["1","2"])

            if acao == "1":
                dano = max(0, robo['ataque'] - jogador['defesa'])
                jogador['hp'] -= dano
                print(f"Você recebeu {dano} de dano!")
                print(f"Você ficou com {jodador['hp']} de vida")
            else:
                cura = 20
                robo['hp'] = min(hp,robo['hp']+cura) # pegar o menor valor entre os dois
                print("O robo se curou")
                print(f"O robo está com {robo['hp']} de vida")

            if jogador['hp'] <= 0:
                print("Você perdeu!")
                break

