def calcula_tres(p1,p2,p3):
    soma=p1+p2+p3
    return soma
if __name__=='__main__':
    valor1=int(input('Digite o primeiro valor: '))
    valor2=int(input('Digite o segundo valor: '))
    valor3=int(input('Digite o terceiro valor: '))
    resultado=calcula_tres(valor1,valor2,valor3)
    print(f'{valor1} + {valor2} + {valor3} = {resultado}')