arquivo = open("criptografado.txt", "r", encoding="utf-8")
mensagem = arquivo.read()
arquivo.close()

mensagem_descriptografada = ""

for letra in mensagem:
    if 'a' <= letra <= 'z':
        codigo = ord(letra) - 3 #ord é para pegar o valor ASCII do caractere
        if codigo < ord('a'):
            codigo = codigo + 26
        mensagem_descriptografada = mensagem_descriptografada + chr(codigo)

    elif 'A' <= letra <= 'Z':
        codigo = ord(letra) - 3
        if codigo < ord('A'):
            codigo = codigo + 26
        mensagem_descriptografada = mensagem_descriptografada + chr(codigo)

    else:
        mensagem_descriptografada = mensagem_descriptografada + letra

print(mensagem_descriptografada)
