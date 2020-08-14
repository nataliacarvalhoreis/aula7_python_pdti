class Bola:

    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def troca_cor(self, cor):
        self.__cor = cor

    def motrar_cor(self):
        return self.__cor

#testando a classe

bola_futebol = Bola('branca', 3.5, 'couro')
print(bola_futebol.motrar_cor())
bola_futebol.troca_cor('verde')
print(bola_futebol.motrar_cor())