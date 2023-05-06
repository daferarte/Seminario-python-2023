# cracion de funcion simple
"""
def multiplicacion():
    print(f'la multiplicacion de 7X7 es igual a {7*7}')
"""
# metodo para multiplicar dos parametros
def multiplicacion(a,b):
    # multiplicacion 
    print(f'la multiplicacion de {a}X{b} es igual a {a*b}')
    # comprobacion de par
    print(f'Y este resultado es par: {par(a*b)}')

# evalua si un numero es par o impar
def par(a):
    # sentencia if = si % = reciduo de divicion retunr mensaje
    if (a % 2) == 0:
        return 'par'
    else:
        return 'impar'

print('inicia el software')
# llamado de la funcion
multiplicacion(3,4)
print('siguiente')
multiplicacion(5,5)