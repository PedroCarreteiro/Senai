import random

itens = {
    "1":{
        "nome": "Poção de força",
        "efeito": "ataque+20",
        "turnos": 2
    },
    "2":{
        "nome": "Bola de fogo",
        "efeito": "dano explosivo ao inimigo",
        "turnos": 1
    }
}

duracao_item_jogador = 0
duracao_item_robo = 0
item_jogador = ""
item_robo = ""

itens_gastos_jogador = []
itens_gastos_robo = []

efeitos =

while True:

    opcao = input("Iniciar [1]\n"
                  "Multiplayer [2]\n"
                  "Sair [3]")

    if opcao == "2":
        multiplayer = True
    else:
        multiplayer = False

    if opcao == "3":
        break

    elif opcao == "1" or opcao == "2":
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
            print(f"Ataque inimigo: {robo['ataque']}  Defesa inimigo: {robo['defesa']}")

            acao = input("[1] para atacar [2] para curar [3] para item [4] para efeito de status: ")

            if acao == "1":
                dano = max(0,jogador['ataque']-robo['defesa'])
                if random.random() < 0.1: #sortear numero entre 0 e 1
                    dano *= 2
                    print("Dano crítico!")
                robo['hp'] -= dano
                print(f"Você causou {dano} de dano!")
                print(f"O inimigo ficou com {robo['hp']} de vida")
            elif acao == "2":
                cura = 20
                if cura + jogador['hp'] > hp:
                    jogador['hp'] = hp
                else:
                    jogador['hp'] += cura

            elif acao == "3":
                print("Items disponíveis: ")
                for chave, valor in items():
                    print(f"[{chave}] {valor['nome']} - {valor['efeito']}")
                escolha_item = input("Escolha seu item: ")
                if escolha_item == "1" and "1" not in itens_gastos_jogador:
                    jogador["ataque"] += 20
                    duracao_item = 2
                    item_jogador = "1"
                    itens_gastos_jogador.append("1")
                elif escolha_item == "2" and "2" not in itens_gastos_jogador:
                    robo['hp'] -= 50
                    duracao_item_jogador = 1
                    itens_gastos_jogador.append("2")
            elif acao == "4":
                escolha_status = input("Você pode selecionar os efeitos: "
                      "\n[1] buffer overflow"
                      "\n[2] loop infinito"
                      "\n[3] tela azul"
                      "\n[4] cache hit")
                if escolha_status == "1" or escolha_status == "2" or escolha_status == "3":
                    efeitos['robo'].append(escolha_status)
                elif escolha_status == "4":
                    efeitos['jogador'].append("4")




            if duracao_item_jogador > 0:
                duracao_item_jogador -= 1
            elif item_jogador == "1":
                jogador["ataque"] -= 20
                item_jogador = ""

            if robo['hp'] <= 0:
                print("Você venceu!")
                break

            if multiplayer:
                acao = input('[1] atacar [2] curar: ')
            else:
                acao = random.choice(["1","2"])

            if acao == "1":
                dano = max(0, robo['ataque'] - jogador['defesa'])
                if random.random() < 0.1: #sortear numero entre 0 e 1
                    dano *= 2
                    print("Dano crítico inimigo!")
                jogador['hp'] -= dano
                print(f"Você recebeu {dano} de dano!")
                print(f"Você ficou com {jogador['hp']} de vida")
            else:
                cura = 20
                robo['hp'] = min(hp,robo['hp']+cura) # pegar o menor valor entre os dois
                print("O robo se curou")
                print(f"O robo está com {robo['hp']} de vida")

            if jogador['hp'] <= 0:
                print("Você perdeu!")
                break

