import random
from random import randint

iniciar = 1

while iniciar == 1:
    #Iniciar o jogo
    iniciar = int(input("Selecione uma das opções: \n"
                       "Iniciar [1]\n"
                       "Sair [2]\n"))

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

        #Começar o jogo
        while True:

            turno += 1

            cura = 20

            print(f"--- Turno {turno} ---\n"
                  f"Seu HP: {vida_jogador} | Inimigo HP: {vida_cpu}")
            opcao = int(input("Sua vez: [1] Atacar ou [2] Curar? "))

            #Se atacar selecionado
            if opcao == 1:
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


            #Sorteio da ação da cpu:
            opcao_cpu = randint(1,2)

            # Se atacar sortado
            if opcao_cpu == 1:
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

    #Se sair selecionado
    elif iniciar == 2:
        print("Você saiu do jogo!")



    #Se outra opcao selecionada:
    else:
        print("INVALIDO")


