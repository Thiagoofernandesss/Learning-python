# T h i a g o
# 0 1 2 3 4 5
# -6 -5 -4 -3 -2 -1
nome = 'Thiago'

# print(nome[0])
# print(nome[-5])

# print('i' in nome)
# print('u' in nome)
# print('To' in nome)

    
nome = input('Digite seu nome: ')
encontrar = input('Digite oque você deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em nome')

