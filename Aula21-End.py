entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')

senhaCorreta = '123'

if(entrada == 'E' and senha == senhaCorreta):
    print('Entrar')
else:
    print('Sair')