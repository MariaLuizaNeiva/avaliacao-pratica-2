par=0
impar=0
soma=0
print('Digite 0 para sair.')
while True:
    numero=int(input('Digite um número: '))
    if numero==0:
        break
    if numero%2==0:
        par=par+1
        soma=soma+1
    if numero%2!=0:
        impar=impar+1
        soma=soma+1
media_par=soma/par if par>0 else 0
media_impar=soma/impar if impar>0 else 0
print(f'Foram digitados {par} números pares e {impar} números ímpares.'
      f'\nA média dos números pares é igual à {media_par}.'
      f'\nA média dos números ímpares é igual à {media_impar}.')