frase = input("Digite uma frase: ")
frase_formatada = frase.lower()


contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

tamanho = len(frase)

for i in range (0,tamanho):
    if frase_formatada[i] == "a":
        contador_a += 1
    if frase_formatada[i] == "e":
        contador_e += 1
    if frase_formatada[i] == "i":
        contador_i += 1
    if frase_formatada[i] == "o":
        contador_o += 1
    if frase_formatada[i] == "u":
        contador_u += 1

print(f"O total de 'a' na frase é {contador_a}\n"
      f"O total de 'e' na frase é {contador_e}\n"
      f"O total de 'i' na frase é {contador_i}\n"
      f"O total de 'o' na frase é {contador_o}\n"
      f"O total de 'u' na frase é {contador_u}\n")