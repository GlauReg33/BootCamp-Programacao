a = 1
print(type(a))

a = "Maria"
print(type(a))

class Ave():
    def andar(sel):
        print('andando')
    
    def voar(self):
        print('voando')

class Calopsita(Ave):
        def piar(self):        
         print('piuuuu')

class Pato(Ave):
    def quack(self):
        print('quack')

    def nadar(self):
        print('nadar')  

def executar_pato(animal):
        animal.quack()
        animal.andar()
        animal.voar()
        animal.nadar()           

Pato = Pato()
Calopsita = Calopsita()

executar_pato(Pato)
    
