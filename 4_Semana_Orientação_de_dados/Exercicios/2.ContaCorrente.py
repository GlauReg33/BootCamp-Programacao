# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal


class ContaCorrente:
    def __init__(self, clientes):
        self.clientes = clientes
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Depósito: +{valor}")

    def sacar(self, valor):
        if self._pode_sacar(valor):
            self.saldo -= valor
            self.operacoes.append(f"Saque: -{valor}")
        else:
            print("Saldo insuficiente")

    def _pode_sacar(self, valor):
        if isinstance(self.clientes[0], Cliente):
            cliente = self.clientes[0]
            if cliente.renda_mensal >= 0 and valor <= self.saldo:
                return True
            elif cliente.renda_mensal < 0 and valor <= self.saldo - cliente.renda_mensal:
                return True
        return False

cliente1 = Cliente("Maria", "123456789", 2500)
cliente2 = Cliente("João", "987654321", 3000)

conta1 = ContaCorrente([cliente1])
conta2 = ContaCorrente([cliente2])

conta1.depositar(1000)
conta1.sacar(500)
conta1.sacar(2000)  # Saldo insuficiente

conta2.depositar(1500)
conta2.sacar(2000)  # Saldo insuficiente

print(conta1.saldo)  # 500
print(conta2.saldo)  # 1500
print(conta1.operacoes)  # ['Depósito: +1000', 'Saque: -500']
print(conta2.operacoes)  # ['Depósito: +1500']