"""
nome1 = "aula"
nome2 = "Python"
exemplo = "t"

print(nome1+nome2)

exemplo = nome1
nome1 = nome2
nome2 = exemplo


print(nome1+nome2)
"""

nome1 = "aula"
nome2 = "Python"

print(nome1+nome2)

nome1,nome2 = nome2,nome1

print(nome1+nome2)