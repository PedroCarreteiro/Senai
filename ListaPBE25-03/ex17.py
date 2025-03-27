data = input("Digite a data em dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

print(dia,mes,ano)

if mes <= 12 and mes > 0:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if mes == 1:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 2:
            if dia == 29:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 3:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 4:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 5:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 6:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 7:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 8:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 9:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 10:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 11:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 12:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
     
    elif (ano % 4 != 0 and ano % 100 == 0) or (ano % 400 != 0):
        if mes == 1:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 2:
            if dia == 28:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 3:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 4:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 5:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 6:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 7:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 8:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 9:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 10:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 11:
            if dia == 31:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
        elif mes == 12:
            if dia == 30:
                data_formatada = (data[6:10] + "-" + data[3:5] + "-" + data[0:2])
                print(f"A data formatada é {data_formatada}")
            else:
                print("O dia está incorreto!")
                
else:
    print("O mês está incorreto!")
