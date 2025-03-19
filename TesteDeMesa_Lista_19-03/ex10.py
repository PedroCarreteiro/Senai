prova1 = float(input("Digite a nota da prova 1: "))
prova2 = float(input("Digite a nota da prova 2: "))
prova3 = float(input("Digite a nota da prova 3: "))

if prova1 < prova2 and prova1 < prova3:
    media = (prova2 + prova3) / 2
    print("A primeira nota foi descartada")
    print(f"A media é {media}")
elif prova2 < prova1 and prova2 < prova3:
    media = (prova1 + prova3) / 2
    print("A segunda nota foi descartada")
    print(f"A media é {media}")
elif prova3 < prova1 and prova3 < prova2:
    media = (prova1 + prova2) / 2
    print("A terceira nota foi descartada")
    print(f"A media é {media}")