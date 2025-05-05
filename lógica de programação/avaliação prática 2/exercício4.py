x=float(input('Digite o primeiro número: '))
y=float(input('Digite o segundo número: '))
operacao=str(input('Qual operação você deseja realizar: +,-,*,/? '))
if operacao=='+':
    print(f'{x} + {y} = {x+y}.')
elif operacao=='-':
    print(f'{x} - {y} = {x-y}.')
elif operacao=='*':
    print(f'{x} * {y} = {x*y}.')
else:
    print(f'{x} / {y} = {x/y}.')