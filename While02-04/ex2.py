i = 0
lista = []

while i < 5:
    i+=1
    numero = input(f"Digite o {i}° número: ")
    float(numero)
    lista.insert(0, numero)

print(lista)
print("O maior número é: "+max(lista))

