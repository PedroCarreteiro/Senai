#comandos
#.bibloteca json
#.with open()
#.writer
#.writerow
#.reader()

import json

# data = {
#         "nome": "João",
#         "idade": 18,
#     }
#
# json_string = json.dumps(data)

with open("dados.json", "w") as arquivo_json: #o w é para write, o r é para read
    json.dump({"Nome":"João", "Idade":25}, arquivo_json)
    arquivo_json.close()

with open ("dados.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)
    arquivo_json.close()
