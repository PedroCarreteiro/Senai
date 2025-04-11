# 10 - Números de Kaprekar

kaprekar = []

inicio = int(input("Digite o início do intervalo que deseja verificar: "))
fim = int(input("Digite o fim do intervalo que deseja verificar: "))

for numero in range(inicio, fim + 1):
    verificacao = "{:02d}".format(numero ** 2)

    # Separando em direita e esquerda
    esquerda = []

    for char in range(len(verificacao) // 2):
        esquerda.append(verificacao[char])

    direita = []

    for char in range(len(verificacao) // 2, len(verificacao)):
        direita.append(verificacao[char])

    d = ""

    esquerda = int(d.join(esquerda))
    direita = int(d.join(direita))

    numero_final = esquerda + direita

    if numero_final == numero:
        kaprekar.append(numero_final)

if len(kaprekar) > 0:
    print(f"Os números de Kaprekar no intervalo [{inicio}; {fim}] são {kaprekar}.")
else:
    print(f"Não existem números de Kaprekar no intervalo [{inicio}; {fim}].")
