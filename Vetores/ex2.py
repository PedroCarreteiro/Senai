lista = []

for i in range(1,6):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    lista.append(nota)
    
media = sum(lista) / len(lista)

alunos_acima = []
alunos_abaixo = []
alunos_igual = []

for i in range(1, 6):
    if lista[i-1] > media:
        print(f"A nota do aluno {i} é {lista[i-1]} e sua nota é acima da média!")
        alunos_acima.append(i)
    elif lista[i-1] < media:
        print(f"A nota do aluno {i} é {lista[i-1]} e sua nota é abaixo da média!")
        alunos_abaixo.append(i)
    elif lista[i-1] == media:
        print(f"A nota do aluno {i} é {lista[i-1]} e sua nota é igual à média!")
        alunos_igual.append(i)

print(f"A porcentagem de alunos com nota acima da média é: {((len(alunos_acima) / 5) * 100)}%"
      f"\nA porcentagem de alunos com nota abaixo da média é: {(len(alunos_abaixo) / 5) * 100}%"
      f"\nA porcentagem de alunos com nota igual à média é: {(len(alunos_igual) / 5) * 100}%")