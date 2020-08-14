#Classe Retangulo: Crie uma classe que modele um retangulo:
# A. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# B. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# C. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés
# necessárias para o local.

class Retangulo:

    def __init__(self, ladoA, ladoB):
        self.__ladoA = ladoA
        self.__ladoB = ladoB

    def mudarLados(self, ladoA, ladoB):
        self.__ladoA = ladoA
        self.__ladoB = ladoB

    def retorna_lados(self):
        return self.__ladoA, self.__ladoB

    def calcula_area(self):
        area = self.__ladoA * self.__ladoB
        return area

    def calcula_perimetro(self):
        perimetro = 2*(self.__ladoA + self.__ladoB)
        return perimetro

#testando a classe

ladoA = float(input("Informe o valor do primeiro lado: "))
ladoB = float(input("Informe o valor do segundo lado: "))

primeiro = Retangulo(ladoA, ladoB)
print(f'Área: {primeiro.calcula_area()}')
print(f'Perímetro: {primeiro.calcula_perimetro()}')