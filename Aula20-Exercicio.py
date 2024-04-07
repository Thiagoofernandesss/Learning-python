valor1 = input('Valor 1: ')
valor2 = input('Valor 2: ')

if(valor1>valor2):
    print(f'{valor1=} é maior que {valor2=}')
elif(valor2>valor1):
    print(f'{valor2=} é maior que {valor1=}')
else:
    print(f'{valor1=} é igual que {valor2=}')