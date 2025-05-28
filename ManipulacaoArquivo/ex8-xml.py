#comandos
#.with open()
#.write()
#.read()

with open("config.xml", "w", encoding="utf-8") as arquivo: #o w é para write, o r é para read
    arquivo.write("<config>")
    arquivo.write("<versao>")
    arquivo.write("1.0")
    arquivo.write("</versao>")
    arquivo.write("</config>")

with open("config.xml", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())

#correção

xml_str = """<?xml version="1.0" emcoding="UTF-8"?>
<config>
    <versao>1.0</versao>
</config>"""

with open("config.xml", "w", encoding="utf-8") as f:
    f.write(xml_str)

with open("config.xml", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)