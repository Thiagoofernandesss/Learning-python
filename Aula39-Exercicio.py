nome = 'Luiz Otávio'
nova_string = ''
letra = 0

while letra < len(nome):
    nova_string += nome[letra] + '*'
    letra +=1

print(nova_string)