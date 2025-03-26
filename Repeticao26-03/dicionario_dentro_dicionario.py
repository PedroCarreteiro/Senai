alunos = {
    "123":{
        "nome": "Lucas",
        "idade": 17
    },
    "456":{
        "nome": "Maria",
        "idade": 18
    }
}

print(alunos["123"]["nome"])

for ra, dados in alunos.items():
    print(f"RA: {ra}")
    for chave, valor in dados.items():
        print(f" {chave.capitalize()}: {valor}") #capitalize é para colocar o nome em maíusculo