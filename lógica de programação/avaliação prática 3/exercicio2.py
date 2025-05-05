alunos=0
alunos_aprovados=0
alunos_reprovados=0
print('Digite -1 para sair.')
while True:
    nota=float(input('Digite a nota: '))
    if nota==-1:
        break
    alunos=alunos+1
    if nota>=5:
        alunos_aprovados=alunos_aprovados+1
    else:
     alunos_reprovados=alunos_reprovados+1
print(f'{alunos} alunos fizeram a prova.'
      f'\n{alunos_aprovados} foram aprovados.'
      f'\n{alunos_reprovados} foram reprovados.')