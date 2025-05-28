import json

with open("dados.json", "w") as arquivo_json: #o w é para write, o r é para read
    json.dump({"Nome":"João", "Idade":25}, arquivo_json)
    arquivo_json.close()

with open ("dados.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)
    arquivo_json.close()