# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
# A. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# I. vatipoCombustivel.
# II. lorLitro
# III. quantidadeCombustivel
# B. Possua no mínimo esses métodos:
# I. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de
# litros que foi colocada no veículo
# II. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o
# valor a ser pago pelo cliente.
# III. alterarValor( ) – altera o valor do litro do combustível.
# IV. alterarCombustivel( ) – altera o tipo do combustível.
# V. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na
# bomba.

class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, QuantidadeCombustivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__valorLitro = valorLitro
        self.__QuantidadeCombustivel = QuantidadeCombustivel

    def abastecerPorValor(self, valor):
        quantidadeLitros = valor // self.__valorLitro
        self.alterarQuantidadeCombustivel(quantidadeLitros)
        return float(quantidadeLitros)

    def abastecerPorLitro(self, litros):
        valorPagar = litros // self.__valorLitro
        self.alterarQuantidadeCombustivel(litros)
        return valorPagar

    def alteraValor(self, valor):
        if(valor > 0):
            self.__valorLitro = valor;

    def alterarCombustivel(self, combustivel):
        self.__tipoCombustivel = combustivel

    def alterarQuantidadeCombustivel(self, quantidade):
        if(quantidade <= self.__QuantidadeCombustivel):
            self._QuantidadeCombustivel = self._QuantidadeCombustivel - quantidade
            return True
        else:
            return False

    def retornarBomba(self):
        bomba = f'Combustível: {self._tipoCombustivel} | Valor: R${self.valorLitro} | Quantidade em Bomba: {self._QuantidadeCombustivel} litros'
        return bomba

bomba = bombaCombustivel("gasolina", 4.99, 150)

print(bomba.retornarBomba())
bomba.abastecerPorLitro(10)
print(bomba.retornarBomba())
bomba.abastecerPorValor(55.00)
print(bomba.retornarBomba())