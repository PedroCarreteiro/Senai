numero_inicial = int(input("Digite a quantidade inicial de coelhos: "))
geracoes = int(input("Digite a quantidade de gerações: "))
taxa_reproducao = float(input("Digite a taxa de reprodução em %: "))
taxa_mortalidade = float(input("Digite a taxa de mortalidade em %: "))

populacao = numero_inicial

for i in range(geracoes):
    populacao = populacao + (populacao * (taxa_reproducao / 100))
    populacao = populacao - (populacao * (taxa_mortalidade / 100))

print(f"População final é de {int(populacao)} coelhos")
