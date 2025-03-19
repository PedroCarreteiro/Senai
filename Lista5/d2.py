capital = float(input("Digite o capital: "))
taxa_juros = float(input("Digite a taxa de juros: "))
tempo = float(input("Digite o tempo em anos: "))


montante = capital*(1+(taxa_juros/100))**tempo


print(f"O montante é {montante}")
