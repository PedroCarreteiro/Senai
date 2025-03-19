hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

if hora < 24:
    if minutos < 59:
        if segundos < 59:
            print("Hora é válida")
        else:
            print("Segundos inválidos")
    else:
        print("Minutos inválidos")
else:
    print("Hora inválida")