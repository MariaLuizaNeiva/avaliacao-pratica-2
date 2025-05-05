ct=0
soma=0
cv=0
print('Digite -1 para sair.')
while True:
    numero=int(input('Digite um número: '))
    if numero==-1:
        break
    ct=ct+1
    soma=soma+numero
    if numero>20:
        cv=cv+1
media=soma/ct
print(f'Foram digitados {ct} números.'
      f'\nA soma deles é igual à {soma}.'
      f'\nA média deles é {media}.'
      f'\n{cv} deles são maiores que 20.')