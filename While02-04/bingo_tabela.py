import random
from random import randint

acertou = 0
tentativas = 0

cartela = random.sample(range(1,90),25)
print(cartela)

resultados = []

while acertou != 25:
    numero = randint(1, 90)
    if numero not in resultados:
        tentativas+=1
        resultados.append(numero)
        if numero in cartela:
            acertou+=1

print(f"Demorou {tentativas} sorteios para completar a tabela.")
