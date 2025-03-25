import re

cpf = input("Digite seu CPF: ")

cpf_regex = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"

if re.match(cpf_regex, cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) == 11:
        numero1 = int(cpf[0]) * 10
        numero2 = int(cpf[1]) * 9
        numero3 = int(cpf[2]) * 8
        numero4 = int(cpf[3]) * 7
        numero5 = int(cpf[4]) * 6
        numero6 = int(cpf[5]) * 5
        numero7 = int(cpf[6]) * 4
        numero8 = int(cpf[7]) * 3
        numero9 = int(cpf[8]) * 2
        numero10 = int(cpf[9])
        numero11 = int(cpf[10])
        soma = numero1+numero2+numero3+numero4+numero5+numero6+numero7+numero8+numero9
        resto = soma % 11
        if resto < 2 and numero10 == 0:
            numero11 = int(cpf[0]) * 11
            numero21 = int(cpf[1]) * 10
            numero31 = int(cpf[2]) * 9
            numero41 = int(cpf[3]) * 8
            numero51 = int(cpf[4]) * 7
            numero61 = int(cpf[5]) * 6
            numero71 = int(cpf[6]) * 5
            numero81 = int(cpf[7]) * 4
            numero91 = int(cpf[8]) * 3
            numero10 = int(cpf[9]) * 2
            numero111 = int(cpf[10])
            soma1 = numero11 + numero21 + numero31 + numero41 + numero51 + numero61 + numero71 + numero81 + numero91 + numero10
            resto1 = soma1 % 11
            if resto1 < 2 and numero111 == 0:
                print("CPF válido!")
            elif 11-resto1 == numero111:
                print("CPF válido!")
            else:
                print("CPF inválido!")
        elif 11-resto == numero10:
            numero11 = int(cpf[0]) * 11
            numero21 = int(cpf[1]) * 10
            numero31 = int(cpf[2]) * 9
            numero41 = int(cpf[3]) * 8
            numero51 = int(cpf[4]) * 7
            numero61 = int(cpf[5]) * 6
            numero71 = int(cpf[6]) * 5
            numero81 = int(cpf[7]) * 4
            numero91 = int(cpf[8]) * 3
            numero10 = int(cpf[9]) * 2
            numero111 = int(cpf[10])
            soma2 = numero11 + numero21 + numero31 + numero41 + numero51 + numero61 + numero71 + numero81 + numero91 + numero10
            resto2 = soma2 % 11
            if resto2 < 2 and numero111 == 0:
                print("CPF válido!")
            elif 11 - resto2 == numero111:
                print("CPF válido!")
            else:
                print("CPF inválido!")
        else:
            print("CPF inválido!")
    else:
        print("Tamanho do CPF inválido!")
else:
    print("Formato do CPF inválido!")
