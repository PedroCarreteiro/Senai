pessoa = {
    "nome": "Ana",
    "idade":30,
    "profisão":"Engenheira"
}

print(pessoa["nome"])
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
    
print("Outra parte")

for chave, valor in pessoa.items():
    if chave == "nome":
        print(f"{chave}: valor")
    print("Acabou o IF")
print("Acabou o FOR")