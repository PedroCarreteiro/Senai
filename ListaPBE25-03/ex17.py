data = input("Digite a data em dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])

if mes <= 12 and mes > 0:
    if dia >= 28 and dia < 32:
        data_formatada = (data[6:10]+"-"+data[3:5]+"-"+data[0:2])
        print(f"A data formatada é {data_formatada}")
    else:
        print("O dia está incorreto!")
else:
    print("O mês está incorreto!")
