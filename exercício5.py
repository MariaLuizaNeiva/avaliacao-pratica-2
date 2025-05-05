x=int(input('Digite o valor da primeira reta: '))
y=int(input('Digite o valor da segunda reta: '))
z=int(input('Digite o valor da terceira reta: '))
if x>=(y+z) or y>=(x+z) or z>=(x+y):
    print('Não é um triângulo.')
elif x==y==z:
    print('É um triângulo equilátero.')
elif x==y or x==z or y==z:
    print('É um triângulo isósceles.')
else:
    print('É um triângulo escaleno.')