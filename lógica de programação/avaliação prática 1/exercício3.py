import math
x_um=int(input('X1= '))
x_dois=int(input('X2= '))
y_um=int(input('Y1= '))
y_dois=int(input('Y2= '))
distancia=math.sqrt(((x_dois-x_um)**2)+((y_dois-y_um)**2))
print(f'A distância entre os pontos cartesianos é de {distancia:.2f}.')