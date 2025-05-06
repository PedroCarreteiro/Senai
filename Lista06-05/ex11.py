palavra_1 = "Ana Ana"
palavra_2 = "1DSTB-SENAI"
palavra_3 = "Subi no Onibus"

palavra_1_lower = palavra_1.lower()
palavra_2_lower = palavra_2.lower()
palavra_3_lower = palavra_3.lower()

palavra_1_espaco = palavra_1_lower.replace(" ","")
palavra_2_espaco = palavra_2_lower.replace(" ","")
palavra_3_espaco = palavra_3_lower.replace(" ","")

palindromo_palavra_1 = palavra_1_espaco[::-1]
palindromo_palavra_2 = palavra_2_espaco[::-1]
palindromo_palavra_3 = palavra_3_espaco[::-1]


if palavra_1_espaco == palindromo_palavra_1:
    print(f"A palavra {palavra_1} é um palíndromo!")
else:
    print(f"A palavra {palavra_1} não é um palíndromo!")

if palavra_2_espaco == palindromo_palavra_2:
    print(f"A palavra {palavra_2} é um palíndromo!")
else:
    print(f"A palavra {palavra_2} não é um palíndromo!")

if palavra_3_espaco == palindromo_palavra_3:
    print(f"A palavra {palavra_3} é um palíndromo!")
else:
    print(f"A palavra {palavra_3} não é um palíndromo!")