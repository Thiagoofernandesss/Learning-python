"""
try/except
try-> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(123)
# print(456)
# int('a')

numero_str = input('Vou dobrar o número que você digitar:')

try:
    print('STR:',numero_str)
    numero_float = float(numero_str)
    print('Float:',numero_float)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
except:
    print('Não é um número')