import random
from random import randint

iniciar = 1

while iniciar == 1 or iniciar == 2:
    #Iniciar o jogo
    iniciar = int(input("Selecione uma das opções: \n"
                       "Iniciar [1]\n"
                       "Iniciar PVP [2]"
                       "Sair [3]\n"))

    #Se iniciar selecionado
    if iniciar == 1:

        # Definir a vida
        vida_inicio = randint(200,1000)
        vida_jogador = vida_inicio
        vida_cpu = vida_inicio

        # Definir o dano
        dano_jogador = randint(1, 50)
        dano_cpu = randint(1, 50)

        # Definir a defesa
        defesa_jogador = randint(1, 50)
        defesa_cpu = randint(1, 50)

        #Imprimir status inciais
        print(f"=== DUELO DE HERÓIS ===\n"
                  f"=== Você            ===\n"
                  f"HP: {vida_jogador}     \n"
                  f"ATQ: {dano_jogador}   DEF: {defesa_jogador}\n\n"
                  f"=== Inimigo         ===\n"
                  f"HP: {vida_cpu}     \n"
                  f"ATQ: {dano_cpu}   DEF: {defesa_cpu}\n\n")

        #Definir o contador de turnos como 0
        turno = 0

        # Condição de acionamento de efeitos
        buffer_selecionado = False
        loop_selecionado = False
        azul_selecionado = False

        # Definir a condição dos itens
        roma = True
        orbe = True
        manto = True
        autoridade = True

        # Definir condição dos efeitos
        buffer = True
        loop = True
        azul = True
        hit = True

        #Começar o jogo
        while True:


            #Se buffer estiver ativo
            if buffer_selecionado:
                vida_cpu -= vida_inicio * 0.05

            #Se tela azul estiver ativo
            if azul_selecionado:

                #Contador da tela zul
                contador_azul = 0

                while contador_azul != 2:

                    turno += 1

                    cura = 20

                    #Zerar a defesa da cpu
                    defesa_cpu = 0

                    print(f"--- Turno {turno} ---\n"
                          f"Seu HP: {vida_jogador} | Inimigo HP: {vida_cpu}")

                    # Opcão de itens
                    itens = int(input("Caso queira, utilize um item: \n"
                                      "Romã do castelo do fogo branco (Sua vida atual aumenta em 10%) [1]\n"
                                      "Orbe das chamas (Seu próximo ataque irá causar o total de dano x 2) [2]\n"
                                      "Manto do cavaleiro negro (Sua defesa irá duplicar neste turno) [3]\n"
                                      "Autoridade do monarca (Use apenas em uma situação emergencial!) [4]\n"
                                      "Não quero usar item [0]\n"))  # Segunda vida, mas com apenas 20% da vida máxima

                    # Se item 1 selecionado
                    if itens == 1:
                        # Se roma não estiver sido selecionada ainda, estará true
                        if roma:
                            vida_jogador = vida_jogador + (vida_jogador * 0.10)
                            roma = False
                            print("Romã do castelo do fogo branco utilizada!")
                        else:
                            print("Você já utilizou esse item este jogo!")

                    # Se item 2 selecionado
                    elif itens == 2:
                        # Se orbe não estiver sido selecionada ainda, estará true
                        if orbe:
                            dano_jogador *= 2
                            orbe = False
                            print("Orbe das chamas utilizado!")
                        else:
                            print("Você já utilizou esse item este jogo!")

                    # Se item 3 selecionado
                    elif itens == 3:
                        # Se manto não estiver sido selecionada ainda, estará true
                        if manto:
                            defesa_jogador *= 2
                            manto = False
                            print("Manto do cavaleiro negro utilizado!")
                        else:
                            print("Você já utilizou esse item este jogo!")

                    # Se item 4 selecionado
                    elif itens == 4:
                        # Se autoridade não estiver sido selecionada ainda, estará true
                        if autoridade:
                            # Se estiver em uma situação emergencial
                            if vida_jogador <= vida_jogador * 0.10:
                                vida_jogador = vida_inicio * 0.20
                                autoridade = False
                                print("Autoridade do monarca utilizada!")
                            else:
                                print("Você não está em uma situação emergencial!")
                        else:
                            print("Você já utilizou esse item este jogo!")

                    # Se não quero usar selecionado:
                    elif itens == 0:
                        print("Nenhum item utilizado")

                    # Se nenhuma selecionada
                    else:
                        print("INVALIDO")
                        break

                    # Opção de efeitos de status
                    efeitos = int(input("Caso queira, utilize efeito de status: \n"
                                        "Buffer Overflow (A cada turno, o inimigo sofre dano equivalente a 5% de seu hp máximo) [1]\n"
                                        "Loop Infinito (O próximo turno do inimigo será pulado) [2]\n"
                                        "Cache Hit (Recupera 30% do HP máximo (Só pode ser usado com o HP abaixo de 25%)) [3]\n"
                                        "Não quero utilizar efeito [0]\n"))

                    # Condição de acionamento de efeitos
                    buffer_selecionado = False
                    loop_selecionado = False

                    # Se efeito 1 selecionado
                    if efeitos == 1:
                        # Se buffer não estiver sido selecionado ainda, estará true
                        if buffer:
                            buffer_selecionado = True
                            buffer = False
                            print("Buffer Overflow utilizado!")
                        else:
                            print("Você já utilizou esse efeito este jogo!")

                    # Se efeito 2 selecionado
                    elif efeitos == 2:
                        # Se loop não estiver sido selecionado ainda, estará true
                        if loop:
                            loop_selecionado = True
                            loop = False
                            print("Loop Infinito utilizado!")
                        else:
                            print("Você já utilizou esse efeito este jogo!")

                    # Se efeito 3 selecionado
                    elif efeitos == 3:
                        # Se azul não estiver sido selecionada ainda, estará true
                        if hit:
                            # Se estiver em uma situação emergencial
                            if vida_jogador <= vida_jogador * 0.25:
                                vida_jogador += vida_inicio * 0.30
                                hit = False
                                print("Cache Hit utilizado!")
                            else:
                                print("Você não está com o HP abaixo de 25%!")
                        else:
                            print("Você já utilizou esse efeito este jogo!")

                    # Se não quero usar selecionado:
                    elif efeitos == 0:
                        print("Nenhum efeito utilizado")

                    # Se nenhuma selecionada
                    else:
                        print("INVALIDO")
                        break

                    opcao = int(input("Sua vez: [1] Atacar ou [2] Curar? "))

                    # Se atacar selecionado
                    if opcao == 1:

                        # Chance de ataque critico
                        critico_jogador = randint(1, 10)
                        if critico_jogador == 1:
                            dano_jogador *= 2

                        # Resultado do ataque do jogador
                        ataque_jogador = dano_jogador - defesa_cpu

                        # Se o ataque for menor que 0
                        if ataque_jogador < 0:
                            ataque_jogador = 0

                        print(f"Você ataca! Inimigo perde {ataque_jogador} HP")

                        # Atualizar a vida da cpu
                        vida_cpu = vida_cpu - ataque_jogador

                    # Se curar selecionado
                    elif opcao == 2:

                        # Se o total vida_jogador + cura for menor ou igual que a vida_inicio
                        if vida_jogador + cura <= vida_inicio:
                            print(f"Você se cura em 20 HP!")
                            vida_jogador += cura

                        # Se o total vida_jogador + cura for maior que vida_inicio
                        elif vida_jogador + cura > vida_inicio:
                            cura_menor = vida_inicio - vida_jogador
                            vida_jogador += cura_menor
                            print(f"Você se cura em {cura_menor} HP")

                    # Se nenhuma das opções selecionadas
                    else:
                        print("INVALIDO")
                        break

                    # Se o loop for selecionado
                    if loop_selecionado:
                        print("A CPU reiniciou o sistema!")

                    else:
                        # Sorteio da ação da cpu:
                        opcao_cpu = randint(1, 2)
                        # Se atacar sortado
                        if opcao_cpu == 1:

                            # Chance de ataque crítico
                            critico_cpu = randint(1, 10)
                            if critico_cpu == 1:
                                dano_cpu *= 2

                            # Resultado do ataque do cpu
                            ataque_cpu = dano_cpu - defesa_jogador

                            # Se o ataque for menor que 0
                            if ataque_cpu < 0:
                                ataque_cpu = 0

                            print(f"Inimigo ataca! Você perde {ataque_cpu} HP")

                            # Atualizar a vida da cpu
                            vida_jogador = vida_jogador - ataque_cpu

                        # Se curar selecionado
                        elif opcao_cpu == 2:

                            # Se o total vida_cpu + cura for menor ou igual que a vida_inicio
                            if vida_cpu + cura <= vida_inicio:
                                print(f"Inimigo se cura em 20 HP!")
                                vida_cpu += cura

                            # Se o total vida_cpu + cura for maior que vida_inicio
                            elif vida_cpu + cura > vida_inicio:
                                cura_menor = vida_inicio - vida_cpu
                                vida_cpu += cura_menor
                                print(f"Inimigo cura em {cura_menor} HP")

            turno += 1

            cura = 20

            print(f"--- Turno {turno} ---\n"
                  f"Seu HP: {vida_jogador} | Inimigo HP: {vida_cpu}")

            #Opcão de itens
            itens = int(input("Caso queira, utilize um item: \n"
                              "Romã do castelo do fogo branco (Sua vida atual aumenta em 10%) [1]\n"
                              "Orbe das chamas (Seu próximo ataque irá causar o total de dano x 2) [2]\n"
                              "Manto do cavaleiro negro (Sua defesa irá duplicar neste turno) [3]\n"
                              "Autoridade do monarca (Use apenas em uma situação emergencial!) [4]\n"
                              "Não quero usar item [0]\n"))  # Segunda vida, mas com apenas 20% da vida máxima


            #Se item 1 selecionado
            if itens == 1:
                #Se roma não estiver sido selecionada ainda, estará true
                if roma:
                    vida_jogador = vida_jogador+(vida_jogador*0.10)
                    roma = False
                    print("Romã do castelo do fogo branco utilizada!")
                else:
                    print("Você já utilizou esse item este jogo!")

            #Se item 2 selecionado
            elif itens == 2:
                # Se orbe não estiver sido selecionada ainda, estará true
                if orbe:
                    dano_jogador *= 2
                    orbe = False
                    print("Orbe das chamas utilizado!")
                else:
                    print("Você já utilizou esse item este jogo!")

            #Se item 3 selecionado
            elif itens == 3:
                # Se manto não estiver sido selecionada ainda, estará true
                if manto:
                    defesa_jogador *= 2
                    manto = False
                    print("Manto do cavaleiro negro utilizado!")
                else:
                    print("Você já utilizou esse item este jogo!")

            # Se item 4 selecionado
            elif itens == 4:
                # Se autoridade não estiver sido selecionada ainda, estará true
                if autoridade:
                    #Se estiver em uma situação emergencial
                    if vida_jogador <= vida_jogador*0.10:
                        vida_jogador = vida_inicio*0.20
                        autoridade = False
                        print("Autoridade do monarca utilizada!")
                    else:
                        print("Você não está em uma situação emergencial!")
                else:
                    print("Você já utilizou esse item este jogo!")

            #Se não quero usar selecionado:
            elif itens == 0:
                print("Nenhum item utilizado")

            #Se nenhuma selecionada
            else:
                print("INVALIDO")
                break

            #Opção de efeitos de status
            efeitos = int(input("Caso queira, utilize efeito de status: \n"
                              "Buffer Overflow (A cada turno, o inimigo sofre dano equivalente a 5% de seu hp máximo) [1]\n"
                              "Loop Infinito (O próximo turno do inimigo será pulado) [2]\n"
                              "Tela Azul (A defesa do inimigo será 0 por 2 turnos) [3]\n"
                              "Cache Hit (Recupera 30% do HP máximo (Só pode ser usado com o HP abaixo de 25%)) [4]\n"
                              "Não quero utilizar efeito [0]\n"))

            # Condição de acionamento de efeitos
            buffer_selecionado = False
            loop_selecionado = False
            azul_selecionado = False

            # Se efeito 1 selecionado
            if efeitos == 1:
                # Se buffer não estiver sido selecionado ainda, estará true
                if buffer:
                    buffer_selecionado = True
                    buffer = False
                    print("Buffer Overflow utilizado!")
                else:
                    print("Você já utilizou esse efeito este jogo!")

            # Se efeito 2 selecionado
            elif efeitos == 2:
                # Se loop não estiver sido selecionado ainda, estará true
                if loop:
                    loop_selecionado = True
                    loop = False
                    print("Loop Infinito utilizado!")
                else:
                    print("Você já utilizou esse efeito este jogo!")

            # Se efeito 3 selecionado
            elif efeitos == 3:
                # Se azul não estiver sido selecionada ainda, estará true
                if azul:
                    azul_selecionado = True
                    azul = False
                    print("Tela azul utilizada!")
                else:
                    print("Você já utilizou esse efeito este jogo!")

            #Se efeito 4 selecionado
            elif efeitos == 4:
                # Se azul não estiver sido selecionada ainda, estará true
                if hit:
                    # Se estiver em uma situação emergencial
                    if vida_jogador <= vida_jogador * 0.25:
                        vida_jogador += vida_inicio * 0.30
                        hit = False
                        print("Cache Hit utilizado!")
                    else:
                        print("Você não está com o HP abaixo de 25%!")
                else:
                    print("Você já utilizou esse efeito este jogo!")

            # Se não quero usar selecionado:
            elif efeitos == 0:
                print("Nenhum efeito utilizado")

            # Se nenhuma selecionada
            else:
                print("INVALIDO")
                break

            opcao = int(input("Sua vez: [1] Atacar ou [2] Curar? "))

            #Se atacar selecionado
            if opcao == 1:

                #Chance de ataque critico
                critico_jogador = randint(1,10)
                if critico_jogador == 1:
                    dano_jogador *= 2

                #Resultado do ataque do jogador
                ataque_jogador = dano_jogador - defesa_cpu

                #Se o ataque for menor que 0
                if ataque_jogador < 0:
                    ataque_jogador = 0

                print(f"Você ataca! Inimigo perde {ataque_jogador} HP")

                #Atualizar a vida da cpu
                vida_cpu = vida_cpu - ataque_jogador

            #Se curar selecionado
            elif opcao == 2:

                #Se o total vida_jogador + cura for menor ou igual que a vida_inicio
                if vida_jogador + cura <= vida_inicio:
                    print(f"Você se cura em 20 HP!")
                    vida_jogador+=cura

                #Se o total vida_jogador + cura for maior que vida_inicio
                elif vida_jogador + cura > vida_inicio:
                    cura_menor = vida_inicio-vida_jogador
                    vida_jogador+=cura_menor
                    print(f"Você se cura em {cura_menor} HP")

            #Se nenhuma das opções selecionadas
            else:
                print("INVALIDO")
                break



            #Se o loop for selecionado
            if loop_selecionado:
                print("A CPU reiniciou o sistema!")

            else:
                # Sorteio da ação da cpu:
                opcao_cpu = randint(1, 2)
                # Se atacar sortado
                if opcao_cpu == 1:

                    #Chance de ataque crítico
                    critico_cpu = randint(1, 10)
                    if critico_cpu == 1:
                        dano_cpu *= 2

                    # Resultado do ataque do cpu
                    ataque_cpu = dano_cpu - defesa_jogador

                    # Se o ataque for menor que 0
                    if ataque_cpu < 0:
                        ataque_cpu = 0

                    print(f"Inimigo ataca! Você perde {ataque_cpu} HP")

                    # Atualizar a vida da cpu
                    vida_jogador = vida_jogador - ataque_cpu

                # Se curar selecionado
                elif opcao_cpu == 2:

                    # Se o total vida_cpu + cura for menor ou igual que a vida_inicio
                    if vida_cpu + cura <= vida_inicio:
                        print(f"Inimigo se cura em 20 HP!")
                        vida_cpu += cura

                    # Se o total vida_cpu + cura for maior que vida_inicio
                    elif vida_cpu + cura > vida_inicio:
                        cura_menor = vida_inicio - vida_cpu
                        vida_cpu+=cura_menor
                        print(f"Inimigo cura em {cura_menor} HP")


            #Condições para finalizar o jogo:

            #Jogador ganhou
            if vida_jogador > vida_cpu and vida_cpu <= 0:
                if vida_jogador == vida_cpu:
                    print("Empate!")
                else:
                    print("Você ganhou!")
                    break

            #Cpu ganhou
            elif vida_cpu > vida_jogador and vida_jogador <= 0:
                if vida_cpu == vida_jogador:
                    print("Empate!")
                else:
                    print("Você perdeu!")
                    break

    elif iniciar == 2:

            # Definir a vida
            vida_inicio = randint(200, 1000)
            vida_jogador = vida_inicio
            vida_cpu = vida_inicio

            # Definir o dano
            dano_jogador = randint(1, 50)
            dano_cpu = randint(1, 50)

            # Definir a defesa
            defesa_jogador = randint(1, 50)
            defesa_cpu = randint(1, 50)

            # Imprimir status inciais
            print(f"=== DUELO DE HERÓIS ===\n"
                  f"=== Você            ===\n"
                  f"HP: {vida_jogador}     \n"
                  f"ATQ: {dano_jogador}   DEF: {defesa_jogador}\n\n"
                  f"=== Inimigo         ===\n"
                  f"HP: {vida_cpu}     \n"
                  f"ATQ: {dano_cpu}   DEF: {defesa_cpu}\n\n")

            # Definir o contador de turnos como 0
            turno = 0

            # Condição de acionamento de efeitos
            buffer_selecionado = False
            loop_selecionado = False
            azul_selecionado = False

            # Definir a condição dos itens
            roma = True
            orbe = True
            manto = True
            autoridade = True

            # Definir condição dos efeitos
            buffer = True
            loop = True
            azul = True
            hit = True

            # Começar o jogo
            while True:

                # Se buffer estiver ativo
                if buffer_selecionado:
                    vida_cpu -= vida_inicio * 0.05

                # Se tela azul estiver ativo
                if azul_selecionado:

                    # Contador da tela zul
                    contador_azul = 0

                    while contador_azul != 2:

                        turno += 1

                        cura = 20

                        # Zerar a defesa da cpu
                        defesa_cpu = 0

                        print(f"--- Turno {turno} ---\n"
                              f"Seu HP: {vida_jogador} | Inimigo HP: {vida_cpu}")

                        # Opcão de itens
                        itens = int(input("Caso queira, utilize um item: \n"
                                          "Romã do castelo do fogo branco (Sua vida atual aumenta em 10%) [1]\n"
                                          "Orbe das chamas (Seu próximo ataque irá causar o total de dano x 2) [2]\n"
                                          "Manto do cavaleiro negro (Sua defesa irá duplicar neste turno) [3]\n"
                                          "Autoridade do monarca (Use apenas em uma situação emergencial!) [4]\n"
                                          "Não quero usar item [0]\n"))  # Segunda vida, mas com apenas 20% da vida máxima

                        # Se item 1 selecionado
                        if itens == 1:
                            # Se roma não estiver sido selecionada ainda, estará true
                            if roma:
                                vida_jogador = vida_jogador + (vida_jogador * 0.10)
                                roma = False
                                print("Romã do castelo do fogo branco utilizada!")
                            else:
                                print("Você já utilizou esse item este jogo!")

                        # Se item 2 selecionado
                        elif itens == 2:
                            # Se orbe não estiver sido selecionada ainda, estará true
                            if orbe:
                                dano_jogador *= 2
                                orbe = False
                                print("Orbe das chamas utilizado!")
                            else:
                                print("Você já utilizou esse item este jogo!")

                        # Se item 3 selecionado
                        elif itens == 3:
                            # Se manto não estiver sido selecionada ainda, estará true
                            if manto:
                                defesa_jogador *= 2
                                manto = False
                                print("Manto do cavaleiro negro utilizado!")
                            else:
                                print("Você já utilizou esse item este jogo!")

                        # Se item 4 selecionado
                        elif itens == 4:
                            # Se autoridade não estiver sido selecionada ainda, estará true
                            if autoridade:
                                # Se estiver em uma situação emergencial
                                if vida_jogador <= vida_jogador * 0.10:
                                    vida_jogador = vida_inicio * 0.20
                                    autoridade = False
                                    print("Autoridade do monarca utilizada!")
                                else:
                                    print("Você não está em uma situação emergencial!")
                            else:
                                print("Você já utilizou esse item este jogo!")

                        # Se não quero usar selecionado:
                        elif itens == 0:
                            print("Nenhum item utilizado")

                        # Se nenhuma selecionada
                        else:
                            print("INVALIDO")
                            break

                        # Opção de efeitos de status
                        efeitos = int(input("Caso queira, utilize efeito de status: \n"
                                            "Buffer Overflow (A cada turno, o inimigo sofre dano equivalente a 5% de seu hp máximo) [1]\n"
                                            "Loop Infinito (O próximo turno do inimigo será pulado) [2]\n"
                                            "Cache Hit (Recupera 30% do HP máximo (Só pode ser usado com o HP abaixo de 25%)) [3]\n"
                                            "Não quero utilizar efeito [0]\n"))

                        # Condição de acionamento de efeitos
                        buffer_selecionado = False
                        loop_selecionado = False

                        # Se efeito 1 selecionado
                        if efeitos == 1:
                            # Se buffer não estiver sido selecionado ainda, estará true
                            if buffer:
                                buffer_selecionado = True
                                buffer = False
                                print("Buffer Overflow utilizado!")
                            else:
                                print("Você já utilizou esse efeito este jogo!")

                        # Se efeito 2 selecionado
                        elif efeitos == 2:
                            # Se loop não estiver sido selecionado ainda, estará true
                            if loop:
                                loop_selecionado = True
                                loop = False
                                print("Loop Infinito utilizado!")
                            else:
                                print("Você já utilizou esse efeito este jogo!")

                        # Se efeito 3 selecionado
                        elif efeitos == 3:
                            # Se azul não estiver sido selecionada ainda, estará true
                            if hit:
                                # Se estiver em uma situação emergencial
                                if vida_jogador <= vida_jogador * 0.25:
                                    vida_jogador += vida_inicio * 0.30
                                    hit = False
                                    print("Cache Hit utilizado!")
                                else:
                                    print("Você não está com o HP abaixo de 25%!")
                            else:
                                print("Você já utilizou esse efeito este jogo!")

                        # Se não quero usar selecionado:
                        elif efeitos == 0:
                            print("Nenhum efeito utilizado")

                        # Se nenhuma selecionada
                        else:
                            print("INVALIDO")
                            break

                        opcao = int(input("Sua vez: [1] Atacar ou [2] Curar? "))

                        # Se atacar selecionado
                        if opcao == 1:

                            # Chance de ataque critico
                            critico_jogador = randint(1, 10)
                            if critico_jogador == 1:
                                dano_jogador *= 2

                            # Resultado do ataque do jogador
                            ataque_jogador = dano_jogador - defesa_cpu

                            # Se o ataque for menor que 0
                            if ataque_jogador < 0:
                                ataque_jogador = 0

                            print(f"Você ataca! Inimigo perde {ataque_jogador} HP")

                            # Atualizar a vida da cpu
                            vida_cpu = vida_cpu - ataque_jogador

                        # Se curar selecionado
                        elif opcao == 2:

                            # Se o total vida_jogador + cura for menor ou igual que a vida_inicio
                            if vida_jogador + cura <= vida_inicio:
                                print(f"Você se cura em 20 HP!")
                                vida_jogador += cura

                            # Se o total vida_jogador + cura for maior que vida_inicio
                            elif vida_jogador + cura > vida_inicio:
                                cura_menor = vida_inicio - vida_jogador
                                vida_jogador += cura_menor
                                print(f"Você se cura em {cura_menor} HP")

                        # Se nenhuma das opções selecionadas
                        else:
                            print("INVALIDO")
                            break

                        # Se o loop for selecionado
                        if loop_selecionado:
                            print("A CPU reiniciou o sistema!")

                        else:
                            # Sorteio da ação da cpu:
                            opcao_cpu = randint(1, 2)
                            # Se atacar sortado
                            if opcao_cpu == 1:

                                # Chance de ataque crítico
                                critico_cpu = randint(1, 10)
                                if critico_cpu == 1:
                                    dano_cpu *= 2

                                # Resultado do ataque do cpu
                                ataque_cpu = dano_cpu - defesa_jogador

                                # Se o ataque for menor que 0
                                if ataque_cpu < 0:
                                    ataque_cpu = 0

                                print(f"Inimigo ataca! Você perde {ataque_cpu} HP")

                                # Atualizar a vida da cpu
                                vida_jogador = vida_jogador - ataque_cpu

                            # Se curar selecionado
                            elif opcao_cpu == 2:

                                # Se o total vida_cpu + cura for menor ou igual que a vida_inicio
                                if vida_cpu + cura <= vida_inicio:
                                    print(f"Inimigo se cura em 20 HP!")
                                    vida_cpu += cura

                                # Se o total vida_cpu + cura for maior que vida_inicio
                                elif vida_cpu + cura > vida_inicio:
                                    cura_menor = vida_inicio - vida_cpu
                                    vida_cpu += cura_menor
                                    print(f"Inimigo cura em {cura_menor} HP")

                turno += 1

                cura = 20

                print(f"--- Turno {turno} ---\n"
                      f"Seu HP: {vida_jogador} | Inimigo HP: {vida_cpu}")

                # Opcão de itens
                itens = int(input("Caso queira, utilize um item: \n"
                                  "Romã do castelo do fogo branco (Sua vida atual aumenta em 10%) [1]\n"
                                  "Orbe das chamas (Seu próximo ataque irá causar o total de dano x 2) [2]\n"
                                  "Manto do cavaleiro negro (Sua defesa irá duplicar neste turno) [3]\n"
                                  "Autoridade do monarca (Use apenas em uma situação emergencial!) [4]\n"
                                  "Não quero usar item [0]\n"))  # Segunda vida, mas com apenas 20% da vida máxima

                # Se item 1 selecionado
                if itens == 1:
                    # Se roma não estiver sido selecionada ainda, estará true
                    if roma:
                        vida_jogador = vida_jogador + (vida_jogador * 0.10)
                        roma = False
                        print("Romã do castelo do fogo branco utilizada!")
                    else:
                        print("Você já utilizou esse item este jogo!")

                # Se item 2 selecionado
                elif itens == 2:
                    # Se orbe não estiver sido selecionada ainda, estará true
                    if orbe:
                        dano_jogador *= 2
                        orbe = False
                        print("Orbe das chamas utilizado!")
                    else:
                        print("Você já utilizou esse item este jogo!")

                # Se item 3 selecionado
                elif itens == 3:
                    # Se manto não estiver sido selecionada ainda, estará true
                    if manto:
                        defesa_jogador *= 2
                        manto = False
                        print("Manto do cavaleiro negro utilizado!")
                    else:
                        print("Você já utilizou esse item este jogo!")

                # Se item 4 selecionado
                elif itens == 4:
                    # Se autoridade não estiver sido selecionada ainda, estará true
                    if autoridade:
                        # Se estiver em uma situação emergencial
                        if vida_jogador <= vida_jogador * 0.10:
                            vida_jogador = vida_inicio * 0.20
                            autoridade = False
                            print("Autoridade do monarca utilizada!")
                        else:
                            print("Você não está em uma situação emergencial!")
                    else:
                        print("Você já utilizou esse item este jogo!")

                # Se não quero usar selecionado:
                elif itens == 0:
                    print("Nenhum item utilizado")

                # Se nenhuma selecionada
                else:
                    print("INVALIDO")
                    break

                # Opção de efeitos de status
                efeitos = int(input("Caso queira, utilize efeito de status: \n"
                                    "Buffer Overflow (A cada turno, o inimigo sofre dano equivalente a 5% de seu hp máximo) [1]\n"
                                    "Loop Infinito (O próximo turno do inimigo será pulado) [2]\n"
                                    "Tela Azul (A defesa do inimigo será 0 por 2 turnos) [3]\n"
                                    "Cache Hit (Recupera 30% do HP máximo (Só pode ser usado com o HP abaixo de 25%)) [4]\n"
                                    "Não quero utilizar efeito [0]\n"))

                # Condição de acionamento de efeitos
                buffer_selecionado = False
                loop_selecionado = False
                azul_selecionado = False

                # Se efeito 1 selecionado
                if efeitos == 1:
                    # Se buffer não estiver sido selecionado ainda, estará true
                    if buffer:
                        buffer_selecionado = True
                        buffer = False
                        print("Buffer Overflow utilizado!")
                    else:
                        print("Você já utilizou esse efeito este jogo!")

                # Se efeito 2 selecionado
                elif efeitos == 2:
                    # Se loop não estiver sido selecionado ainda, estará true
                    if loop:
                        loop_selecionado = True
                        loop = False
                        print("Loop Infinito utilizado!")
                    else:
                        print("Você já utilizou esse efeito este jogo!")

                # Se efeito 3 selecionado
                elif efeitos == 3:
                    # Se azul não estiver sido selecionada ainda, estará true
                    if azul:
                        azul_selecionado = True
                        azul = False
                        print("Tela azul utilizada!")
                    else:
                        print("Você já utilizou esse efeito este jogo!")

                # Se efeito 4 selecionado
                elif efeitos == 4:
                    # Se azul não estiver sido selecionada ainda, estará true
                    if hit:
                        # Se estiver em uma situação emergencial
                        if vida_jogador <= vida_jogador * 0.25:
                            vida_jogador += vida_inicio * 0.30
                            hit = False
                            print("Cache Hit utilizado!")
                        else:
                            print("Você não está com o HP abaixo de 25%!")
                    else:
                        print("Você já utilizou esse efeito este jogo!")

                # Se não quero usar selecionado:
                elif efeitos == 0:
                    print("Nenhum efeito utilizado")

                # Se nenhuma selecionada
                else:
                    print("INVALIDO")
                    break

                opcao = int(input("Sua vez: [1] Atacar ou [2] Curar? "))

                # Se atacar selecionado
                if opcao == 1:

                    # Chance de ataque critico
                    critico_jogador = randint(1, 10)
                    if critico_jogador == 1:
                        dano_jogador *= 2

                    # Resultado do ataque do jogador
                    ataque_jogador = dano_jogador - defesa_cpu

                    # Se o ataque for menor que 0
                    if ataque_jogador < 0:
                        ataque_jogador = 0

                    print(f"Você ataca! Inimigo perde {ataque_jogador} HP")

                    # Atualizar a vida da cpu
                    vida_cpu = vida_cpu - ataque_jogador

                # Se curar selecionado
                elif opcao == 2:

                    # Se o total vida_jogador + cura for menor ou igual que a vida_inicio
                    if vida_jogador + cura <= vida_inicio:
                        print(f"Você se cura em 20 HP!")
                        vida_jogador += cura

                    # Se o total vida_jogador + cura for maior que vida_inicio
                    elif vida_jogador + cura > vida_inicio:
                        cura_menor = vida_inicio - vida_jogador
                        vida_jogador += cura_menor
                        print(f"Você se cura em {cura_menor} HP")

                # Se nenhuma das opções selecionadas
                else:
                    print("INVALIDO")
                    break

                # Se o loop for selecionado
                if loop_selecionado:
                    print("A CPU reiniciou o sistema!")

                else:
                    # Sorteio da ação da cpu:
                    opcao_cpu = randint(1, 2)
                    # Se atacar sortado
                    if opcao_cpu == 1:

                        # Chance de ataque crítico
                        critico_cpu = randint(1, 10)
                        if critico_cpu == 1:
                            dano_cpu *= 2

                        # Resultado do ataque do cpu
                        ataque_cpu = dano_cpu - defesa_jogador

                        # Se o ataque for menor que 0
                        if ataque_cpu < 0:
                            ataque_cpu = 0

                        print(f"Inimigo ataca! Você perde {ataque_cpu} HP")

                        # Atualizar a vida da cpu
                        vida_jogador = vida_jogador - ataque_cpu

                    # Se curar selecionado
                    elif opcao_cpu == 2:

                        # Se o total vida_cpu + cura for menor ou igual que a vida_inicio
                        if vida_cpu + cura <= vida_inicio:
                            print(f"Inimigo se cura em 20 HP!")
                            vida_cpu += cura

                        # Se o total vida_cpu + cura for maior que vida_inicio
                        elif vida_cpu + cura > vida_inicio:
                            cura_menor = vida_inicio - vida_cpu
                            vida_cpu += cura_menor
                            print(f"Inimigo cura em {cura_menor} HP")

                # Condições para finalizar o jogo:

                # Jogador ganhou
                if vida_jogador > vida_cpu and vida_cpu <= 0:
                    if vida_jogador == vida_cpu:
                        print("Empate!")
                    else:
                        print("Você ganhou!")
                        break

                # Cpu ganhou
                elif vida_cpu > vida_jogador and vida_jogador <= 0:
                    if vida_cpu == vida_jogador:
                        print("Empate!")
                    else:
                        print("Você perdeu!")
                        break

    #Se sair selecionado
    elif iniciar == 3:
            print("Você saiu do jogo!")

    #Se outra opcao selecionada:
    else:
        print("INVALIDO")


