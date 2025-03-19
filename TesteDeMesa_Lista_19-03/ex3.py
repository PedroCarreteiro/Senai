quantidade_produtos = int(input("Digite a quantidade de produtos: "))
valor_produto = float(input("Digite o valor do produto: "))
desconto = 0

print(f"O valor inicial é {valor_produto}")
print(f"A quantidade é {quantidade_produtos}")

if quantidade_produtos > 100:
    desconto = (valor_produto / 100)*10
else:
    desconto = (valor_produto / 100) * 5

valor_produto_atualizado = valor_produto - desconto
valor_final = valor_produto_atualizado * quantidade_produtos

print(f"O desconto por unidade é {desconto}")
print(f"O valor atualizado do produto é {valor_produto_atualizado}")
print(f"O valor final é {valor_final}")