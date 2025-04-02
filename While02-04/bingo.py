import random

acertou = 0

cartela = random.sample(range(1,90),25)
print(cartela)

ganhou = False

while acertou != 25:
    numero = random.sample(range(1, 90), 1)
    if numero in cartela:
        print("Você acertou um número!")
        acertou+=1
    else:
        print("Você errou!")
