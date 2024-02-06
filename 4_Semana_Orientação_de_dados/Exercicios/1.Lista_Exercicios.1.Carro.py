# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print("O carro foi ligado.")
        else:
            print("O carro já está ligado.")

    def desliga(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro foi desligado.")
        else:
            print("O carro já está desligado.")

    def acelera(self, valor):
        if self.ligado:
            self.velocidade += valor
            print(f"O carro acelerou. Velocidade atual: {self.velocidade} km/h.")
        else:
            print("Não é possível acelerar o carro desligado.")

    def desacelera(self, valor):
        if self.ligado:
            if self.velocidade >= valor:
                self.velocidade -= valor
            else:
                self.velocidade = 0
            print(f"O carro desacelerou. Velocidade atual: {self.velocidade} km/h.")
        else:
            print("Não é possível desacelerar o carro desligado.")


# Crie uma instancia de classe carro.

# Faça o carro "andar" utilizando os métodos da sua classe.

# Faça o carro "parar" utilizando os métodos da sua classe.
            
meu_carro = Carro("vermelho", "Fusca")

# Ligando o carro
meu_carro.liga()

# Acelerando o carro
meu_carro.acelera(30)

# Desacelerando o carro
meu_carro.desacelera(10)

# Desligando o carro
meu_carro.desliga()