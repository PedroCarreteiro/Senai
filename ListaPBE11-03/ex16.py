import math

x1 = int(input("Digite a coordenada de x1: "))
y1 = int(input("Digite a coordenada de y1: "))
x2 = int(input("Digite a coordenada de x2: "))
y2 = int(input("Digite a coordenada de y2: "))

conta = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"A distância é: {conta}")