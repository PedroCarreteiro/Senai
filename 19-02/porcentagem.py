prestacao = float(input("Digite o valor da prestação: "))
juros = int(input("Digite a porcentagem dos júros: "))

taxa = juros*(prestacao/100)
total = taxa+prestacao

print(f"O valor da taxa é: {taxa} e o total é: {total}")
