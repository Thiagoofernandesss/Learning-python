"""
Fatiamento de String
012345678
Ola mundo
-987654321
Fatiamento [i:f:p] [::]
Obs: A função len retorna a quantidade de caracter de string
"""

variavel = 'Olá Mundo'

print(variavel[2])
print(variavel[4:])
print(variavel[4:8])
print(variavel[:6])
print(len(variavel[3]))
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):2])
print(variavel[::-1])