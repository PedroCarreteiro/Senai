import random

#Lista de palavras
lista_palavras = ["Abacaxi","Banana","Uva","Jabuticaba","Maracujá","Morango","Limão","Laranja"]

#Pegar palavra aleatória da lista e transforma-la em lista
palavra_aleatoria = random.choice(lista_palavras).lower()
lista_palavra_aleatoria = list(palavra_aleatoria)

print(lista_palavra_aleatoria)

#Encriptografar a palavra como ___
lista_palavra_crip = ['_' for _ in palavra_aleatoria]

#Definir a lista com as letras de acertos e erros
lista_chutes = []
lista_erros = []

tentativas = 0

while True:
    chute = input("Digite seu chute: ").lower()
    if chute in lista_chutes:
        print(f"Você já seleciou essa letra antes!\n"
              f"Esses são os seus chutes até agora: {lista_chutes}")
    else:
        if chute in palavra_aleatoria:
            lista_chutes.append(chute)
            #percorrer a palavra e descobrir se tem algo de acordo com  chute
            i = 0
            for letra in lista_palavra_aleatoria:
                if letra == chute: #se a letra naquele i for == chute
                    lista_palavra_crip[i] = chute #revelar o chute na posição do i
                i += 1
            print(f"Você acertou")
        else:
            lista_chutes.append(chute)
            lista_erros.append(chute)
            tentativas += 1

    palavra_atual = ''.join(lista_palavra_crip) #lita em string
    print(f"Essa é a palavra atualmente: {palavra_atual}.\n"
          f"Essas são as letras erradas até agora: {lista_erros}")

    if '_' not in lista_palavra_crip: #se não tem mais _ na lista da palavra encriptada
        print(f"Você ganhou!\n"
              f"A palavra é {palavra_atual}")
        break

    if tentativas >= 6:
        print(f"Você perdeu!\n"
              f"A palavra correta era: {palavra_aleatoria}")
        break


