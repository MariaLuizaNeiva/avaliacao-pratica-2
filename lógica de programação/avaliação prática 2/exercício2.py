x=int(input('Digite o primeiro valor: '))
y=int(input('Digite o segundo valor: '))
z=int(input('Digite o terceiro valor: '))
if x>y>z:
    print(f'O maior valor é {x}.')
elif y>x>z:
    print(f'O maior valor é {y}.')
else:
    print(f'O maior valor é {z}.')