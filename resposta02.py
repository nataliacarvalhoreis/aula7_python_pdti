class Quadrado:

    def __init__(self, lado):
        self.__lado = lado

    def muda_valor(self, lado):
        self.__lado = lado

    def retorna_lado(self):
        return self.__lado

    def calcula_area(self):
        area = self.__lado * self.__lado
        return area

#testando a classe

primeiro = Quadrado(3)

print(primeiro.calcula_area())
primeiro.muda_valor(5)
print(primeiro.retorna_lado())
print(primeiro.calcula_area())