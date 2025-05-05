soma=0
print('Números naturais múltiplos de 3 até 21:')
for n in range (1,22,1):
    if n%3==0:
        print(n)
        soma=soma+n
print(f'Fim da sequência.\nSoma dos números: {soma}.')