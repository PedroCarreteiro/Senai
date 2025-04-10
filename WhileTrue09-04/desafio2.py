import random

lista_palavras = ["Abacaxi","Banana","Uva","Jabuticaba","Maracujá","Morango","Limão","Laranja"]

palavra_aleatoria = random.choice(lista_palavras)
lista_palavra_aleatoria = [char for char in palavra_aleatoria]

palavra_crip = ['_' * len(lista_palavra_aleatoria)]

print(lista_palavra_aleatoria)
print(palavra_crip)
