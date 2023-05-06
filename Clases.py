class Coche:
    #atributos
    ruedas=4
    color=''
    aceleracion=0
    velocidad=0

    #Constructor
    def __init__(self, color, aceleracion):
        self.color=color
        self.aceleracion=aceleracion
        self.velocidad=0

    # metodo
    def acelerar(self):
        # self.velocidad=self.velocidad+self.aceleracion # manera larga de escritura
        self.velocidad+=self.aceleracion # manera corta de escritura
        return self.velocidad
    
class autoVolador(Coche):
    # atributos
    alas=False
    ruedas=6

    # contructor
    def __init__(self, color='verde', aceleracion=10, estaVolando=False):
        super().__init__(color, aceleracion)
        self.estaVolando=estaVolando

    #metodo
    def vuela(self):
        self.estaVolando=True
        return "Estoy Volando"

class moto:
    # atributo
    ruedas=2
    color=''
    aceleracion=0
    velocidad=0
    
    def __init__(self):
        self.color='negro'

# instancia de objeto  
c1=Coche('rojo', 20)
# llamado al objeto
print(c1.color, " ", c1.acelerar())
print(c1.acelerar())

#llamdo coche volador
cv1=autoVolador()
print(cv1.color)
print(cv1.vuela())
print(cv1.acelerar())

# llamado moto
m1=moto();

