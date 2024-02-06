class Quadrado:
    def __init__(self, medida) -> None:
        self.altura = medida
        self.largura = medida

    @property
    def altura(self):
        print('getter de altura')
        return self._medida
    
    @altura.setter
    def altura(self, valor):
        print('setter de altura')
        if valor < 0:
            raise ValueError()
        self._medida = valor
    
    @property
    def largura(self):
        print('getter de largura')
        return self._medida
    
    @largura.setter
    def largura(self, valor):
        print('getter de largura')
        if valor < 0:
            raise ValueError()
        self._medida = valor

    def area(self):
        return self.largura * self.altura
    
quadrado = Quadrado(2)
quadrado.altura = 3
    #print(quadrado.area())
