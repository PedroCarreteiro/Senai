a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))

print(f"O valor de A é {a} e o valor de B é {b}")

a, b = b, a

print(f"O valor de A trocado é {a} e o valor de B trocado é {b}")