#  Classe Conta Corrente: Crie uma classe para implementar uma conta
# corrente. A classe deve possuir os seguintes atributos: número da conta,
# nome do correntista e saldo. Os métodos são os seguintes: alterarNome,
# depósito e saque; No construtor, saldo é opcional, com valor default zero
# e os demais atributos são obrigatórios

class ContaCorrente:

    def __init__(self, numero, correntista, saldo=0):
        self.numero = numero
        self.correntista = correntista
        self.saldo = saldo

    def altera_nome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        if valor>0:
            self.saldo += valor
        else:
            print('Valor precisa ser maior que 0.')

    def saque(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')

#testa classe
conta1 = ContaCorrente('124', 'Natalia')
conta2 = ContaCorrente('122', 'José', 1000.00)

#conta1.saque(300)
conta1.deposito(500)
conta1.saque(150)
print(conta1.saldo)


