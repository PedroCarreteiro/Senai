import random

i = 0
tentativas = 0

while i != 3:
    opcoes = random.choice(["cara", "coroa"])
    print(opcoes)
    if opcoes == "coroa":
        i = 0
    elif opcoes == "cara":
        i+=1
    tentativas += 1

print(f"A quantidade de vezes que a moeda foi lançada para sair 'cara' três vezes seguidas foi de: {tentativas}")