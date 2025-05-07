def maior_n(lista_tamanho):
    lista = []

    for i in range(lista_tamanho):
        i += 1
        numero = float(input(f"Digite o número {i}: "))
        lista.insert(1, numero)
    maior = max(lista)

    print(f"O maior número é {maior}")

lista_tamanho = int(input("Digite o tamanho da lista: "))

maior_n(lista_tamanho)

