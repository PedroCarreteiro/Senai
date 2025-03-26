data = input("Digite a data em dd/mm/aaaa: ")

data_formatada = (data[6:10]+"-"+data[3:5]+"-"+data[0:2])

print(f"Data formatada {data_formatada}")