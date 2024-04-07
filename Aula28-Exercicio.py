nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if nome and idade:
    print('Nome: %s'%(nome))
    print('Nome invertido:%s'%(nome[::-1]))
    
    espaco = 'Não'
    if ' ' in nome:
        espaco = 'Sim'
    print('Tem espaço:%s'%(espaco))
    print('Nº letras:%i'%(len(nome)))
    print('Primeira letra: %s'%(nome[0]))
    print('Última letra:%s'%(nome[len(nome)-1:len(nome)]))
else:
    print('Você deixou campos vazios!')