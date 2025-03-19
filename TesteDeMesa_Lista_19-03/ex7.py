nota = float(input("Digite sua nota: "))

if nota >= 9 and nota <= 10:
    nota_letra = "A"
    print(f"A sua nota é {nota_letra}")
elif nota >= 7 and nota < 9:
    nota_letra = "B"
    print(f"A sua nota é {nota_letra}")
elif nota >= 5 and nota < 7:
    nota_letra = "C"
    print(f"A sua nota é {nota_letra}")
elif nota >= 3 and nota < 5:
    nota_letra = "D"
    print(f"A sua nota é {nota_letra}")
elif nota >= 0 and nota < 3:
    nota_letra = "E"
    print(f"A sua nota é {nota_letra}")
elif nota > 10 or nota < 0:
    nota_letra = "inválida"
    print(f"A sua nota é {nota_letra}")