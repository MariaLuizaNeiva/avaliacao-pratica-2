def mostra_numero(p_numero):
    print(f'Número recebido: {p_numero}')
def mostra_mensagem(p_mensagem):
    print(f'Mensagem recebida: {p_mensagem}')
if __name__=='__main__':
    numero=int(input('Digite um número inteiro: '))
    mensagem=str(input('Digite sua mensagem: '))
    mostra_numero(numero)
    mostra_mensagem(mensagem)