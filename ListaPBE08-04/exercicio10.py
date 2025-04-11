comeco = int(input("Digite um número para começar a verificação: "))
final = int(input("Digite um número para finalizar a verificação: "))

lista_esquerda = []
lista_direita =[]
str_esquerda = ""
str_direita = ""
int_esquerda = 0
int_direita = 0
kaprekar = []
quadrado = 0

if comeco < 0 or final < 0:
    print("INVALIDO")
elif comeco > final:
    print("INVALIDO")
else:
    for numero in range (comeco, final+1):
        
        lista_esquerda = []
        lista_direita =[]
        str_esquerda = ""
        str_direita = ""
        quadrado = int(quadrado)
        quadrado = 0
        
        quadrado = numero**2
        quadrado = str(quadrado)
        
        if len(quadrado) % 2 == 0:
            meio = len(quadrado) / 2
            
            meio = round(meio)
            
            for i in range (0, meio):
                lista_esquerda.append(quadrado[i])
            
            for n in range(meio, len(quadrado)):
                lista_direita.append(quadrado[n])
            
            for elemento_esquerda in lista_esquerda:
                str_esquerda += elemento_esquerda
            
            for elemento_direita in lista_direita:
                str_direita += elemento_direita
            
            int_esquerda = int(str_esquerda)
            int_direita = int(str_direita)
            
            soma = int_direita + int_esquerda
            
            if soma == numero:
                kaprekar.append(numero)
            
        else:
            meio = len(quadrado) / 2
            meio = round(meio)
            
            for i in range(0, meio):
                lista_esquerda.append(quadrado[i])
            
            for n in range (meio, len(quadrado)):
                lista_direita.append(quadrado[n])
            
            for elemento_esquerda in lista_esquerda:
                str_esquerda += elemento_esquerda
            
            for elemento_direita in lista_direita:
                str_direita += elemento_direita
            
            if str_esquerda != '':
                int_esquerda = int(str_esquerda)
                
            int_direita = int(str_direita)
            
            soma = int_direita + int_esquerda
            
            if soma == numero:
                kaprekar.append(numero)
            
    print(kaprekar)
