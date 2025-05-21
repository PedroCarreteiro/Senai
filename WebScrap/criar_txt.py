with open("titulos.txt","w",encoding='utf-8') as f:
    for titulo in titulos:
        f.write(titulo.text.strip() + '\n')