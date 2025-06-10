# importar biblioteca do csv
import csv
# importar biblioteca do date time
from datetime import date
# importar biblioteca do zap
import pywhatkit as kit

# ler arquivo de csv como arquivo
with open("LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv") as arquivo:
    leitor = csv.reader(arquivo)
    # transformar toda a lista do csv em uma lista como dados
    dados = list(leitor)

# selecionar a primeira linha da lista
linha = dados[1:2]

# selecionar apenas a primeira linha, fazendo com que ela seja uma lista
linha_filtrada = linha[0]

# pegar a data da lista
linha_data = linha_filtrada[0]

# #trocar os valores de / por - para não ter conflito com o zap
linha_data = linha_data.replace("/", "-")

# variável para atribuir data atual
data_hoje = date.today()

# transformar data atual em string para verificação no final
data_hoje = str(data_hoje)

# salvar emoticons de cores
# verde = "🟢"
# amarelo = "🟡"
# vermelho = "🔴"
# preto = "⚫"

# verificar a situação de cada estoque e atrinuir a situação neles

estoque = ["⚫","⚫","⚫"]

for i in range(1,4):
    if linha_filtrada[i+1] == "3":
        estoque[i-1] = "🟢"
    elif linha_filtrada[i+1] == "2":
        estoque[i-1] = "🟡"
    elif linha_filtrada[i+1] == "1":
        estoque[i-1] = "🔴"
    elif linha_filtrada[i+1] == "0":
        estoque[i-1] = "⚫"

# verificar se a última data (que é a primeira da lista) é igual a data atual e mandar mensagem
if linha_data == data_hoje:
    kit.sendwhatmsg_instantly("+numero",
                              f"Estoque em {linha_data}: Esteira1: {estoque[0]} | Esteira2: {estoque[1]} | Esteira3: {estoque[2]}")
else:
    kit.sendwhatmsg_instantly("+numero",
                              f"Não foi encontrado nenhum dado do dia atual")
