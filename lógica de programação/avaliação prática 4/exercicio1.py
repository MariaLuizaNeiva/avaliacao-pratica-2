ct=0
print('Números naturais ímpares até 13:')
for n in range (1,14,1):
    if n%2!=0:
        print(n)
        ct=ct+1
print(f'Encerrou a repetição.\nQuantidade: {ct}.')