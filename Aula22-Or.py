entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')

senhaCorreta = '123'

if((entrada == 'E' or entrada=='e') and senha == senhaCorreta):
    print('Entrar')
else:
    print('Sair')