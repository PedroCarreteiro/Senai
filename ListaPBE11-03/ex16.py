import math

x1 = int(input("Digite a coordenada de x1: "))
x2 = int(input("Digite a coordenada de x2: "))
y1 = int(input("Digite a coordenada de y1: "))
y2 = int(input("Digite a coordenada de y2: "))

conta = math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(f"A distância é: {conta}")