def calcula_idade(p_ano):
    i=2025-p_ano
    return i
if __name__=='__main__':
    ano=int(input('Digite o ano do seu nascimento: '))
    idade=calcula_idade(ano)
    print(f'Você tem {idade} anos.')