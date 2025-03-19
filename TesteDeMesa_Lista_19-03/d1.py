import random

numero_pc = random.randint(1,10)

numero_user = int(input("Digite um numero entre 1 e 10: "))

if numero_pc == numero_user:
    print("Você acertou!")

elif numero_pc > numero_user:
    print("O número selecionado é menor que o do computador!")
    numero_user = int(input("Digite um numero entre 1 e 10: "))
    if numero_pc == numero_user:
        print("Você acertou!")
    else:
        print("Você perdeu")


elif numero_pc < numero_user:
    print("O número selecionado é maior que o do computador!")
    numero_user = int(input("Digite um numero entre 1 e 10: "))
    if numero_pc == numero_user:
        print("Você acertou!")
    else:
        print("Você perdeu")