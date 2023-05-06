"""
el ciclo for tiene la siguiente sintaxis:
for elemento in iterable:
    codigo
"""
# uso basico para iteral usando ciclo for
"""
numeros = [8,7,5,8,4,2,5,6,7,0,2,1]

for n in numeros:
    print(n)
"""

# Diccionario en python
valores={
    'A':3,
    'E':4,
    'I':8,
    'O':10,
    'R':11
}

# imprimiendo la llave de un diccionario
"""
for d in valores:
    print(d)
"""
# imprimiendo el valor de un diccionario
"""
for h in valores.values():
    print(h)
"""
# imprimiendo el valor y la llave de un diccionario
"""
for ll, v in valores.items():
    print('ll= ',ll,'| v= ',v)
"""

# for nativo clase range
"""
for i in range(11):
    print(i)
"""
# clase range incremento de valores minimo y un maximo (min, max-1, paso)

for i in range(2,11,2):
    print(i)