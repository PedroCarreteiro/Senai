#importar biblioteca do csv
import csv 
#importar biblioteca do date time
from datetime import date 
#importar biblioteca do zap
import pywhatkit as kit 

#ler arquivo de csv como arquivo
with open("LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv") as arquivo: 
    leitor = csv.reader(arquivo)
    #transformar toda a lista do csv em uma lista como dados
    dados = list(leitor) 

#selecionar a primeira linha da lista
linha = dados[1:2] 

#selecionar apenas a primeira linha, fazendo com que ela seja uma lista
linha_filtrada = linha[0] 

#pegar a data da lista
linha_data = linha_filtrada[0] 

# #trocar os valores de / por - para não ter conflito com o zap
linha_data = linha_data.replace("/","-") 

#variável para atribuir data atual
data_hoje = date.today() 
 
#transformar data atual em string para verificação no final
data_hoje = str(data_hoje) 

#salvar emoticons de cores
# verde = "🟢"
# amarelo = "🟡"
# vermelho = "🔴"
# preto = "⚫"

#verificar a situação de cada estoque e atrinuir a situação neles
if linha_filtrada[2] == "3":
    estoque1 = "🟢"
elif linha_filtrada[2] == "2":
    estoque1 = "🟡"
elif linha_filtrada[2] == "1":
    estoque1 = "🔴"
elif linha_filtrada[2] == "0":
    estoque1 = "⚫"

if linha_filtrada[3] == "3":
    estoque2 = "🟢"
elif linha_filtrada[3] == "2":
    estoque2 = "🟡"
elif linha_filtrada[3] == "1":
    estoque2 = "🔴"
elif linha_filtrada[3] == "0":
    estoque2 = "⚫"

if linha_filtrada[4] == "3":
    estoque3 = "🟢"
elif linha_filtrada[4] == "2":
    estoque3 = "🟡"
elif linha_filtrada[4] == "1":
    estoque3 = "🔴"
elif linha_filtrada[4] == "0":
    estoque3 = "⚫"

#verificar se a última data (que é a primeira da lista) é igual a data atual e mandar mensagem 
if linha_data == data_hoje:
    kit.sendwhatmsg_instantly("+5519971547538",
                            f"Estoque em {linha_data}: Esteira1: {estoque1} | Esteira2: {estoque2} | Esteira3: {estoque3}")
else:
    kit.sendwhatmsg_instantly("+5519971547538",
                            f"Não foi encontrado nenhum dado do dia atual")