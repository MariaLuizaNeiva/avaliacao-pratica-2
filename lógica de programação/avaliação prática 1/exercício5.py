sexo=str(input('Você é homem ou mulher?'))
altura=float(input('Digite sua altura: '))
if sexo == ('homem') or ('Homem'):
    peso_h=(72.7*altura)-58
    print(f'Seu peso ideal é de: {peso_h:.2f}kg.')
else:
    peso_m=(62.1*altura)-44.7
    print(f'Seu peso ideal é de: {peso_m:.2f}kg.')