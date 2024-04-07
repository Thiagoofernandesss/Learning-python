# numero = input('Digite um número inteiro:')


# try:
#     numero_int= int(numero)
#     if numero_int % 2 ==0:
#         print('Número par.')
#     else:
#         print('Número impar.')
# except:
#     print('Não é um número inteiro.')
###############################################

# hora = input('Digite a hora:')

# try:
#     hora_int = int(hora)
    
#     if hora_int <=11:
#         print('Bom dia!')
#     elif hora_int <= 17:
#         print('Boa tarde!')
#     elif hora_int <= 23:
#         print('Boa noite!')
# except:
#     print('Formato de hora incorreto.')

###############################################

nome = input('Digite seu nome:')

numero_letras = len(nome)

if numero_letras<=4:
    print('Nome curto, apenas %i letras.'%(numero_letras))
elif numero_letras<=6:
    print('Nome normal, com %i letras.'%(numero_letras))
else:
    print('Nome grandre, com %i letras.'%(numero_letras))
