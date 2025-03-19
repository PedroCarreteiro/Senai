n1 = float(input("Digite o valor de n1: "))
n2 = float(input("Digite o valor de n2: "))
n3 = float(input("Digite o valor de n3: "))

p1 = float(input("Digite a média ponderada 1: "))
p2 = float(input("Digite o média ponderada 2: "))
p3 = float(input("Digite o média ponderada 3: "))


media = ((n1*p1)+(n2*p2)+(n3*p3)) / (p1+p2+p3)

print(f"A média é: {media:.2f}")