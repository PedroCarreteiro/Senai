def verificar_numero(numero):
    if numero % 2 == 0:
        print("Jogador avança!")
    else:
        print("Jogador recua!")

print(f"O jogador tirou o número 4 e a ação realizada é: {verificar_numero(4)}")
print(f"O jogador tirou o número 7 e a ação realizada é: {verificar_numero(7)}")
print(f"O jogador tirou o número 10 e a ação realizada é: {verificar_numero(10)}")