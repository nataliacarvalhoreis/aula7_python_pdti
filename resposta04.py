# Classe Pessoa: Crie uma classe que modele uma pessoa:
# A. Atributos: nome, idade, peso e altura
# B. Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade
# dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def crescer(self, altura):
        self.__altura += altura
        return self.__altura

    def envelhecer(self, anos):
        idadeAntes = self.__idade
        self.__idade += anos
        if(idadeAntes < 21):
            self.crescer(anos*0.05)
        else:
            self.crescer((21 - idadeAntes)*0.05)
        return self.__idade

    def engordar(self, kilos):
        self.__peso += kilos
        return self.__peso

    def emagrecer(self, kilos):
        self.__peso -= kilos
        return self.__peso

#testa Classe

teste = Pessoa('Natália', 33, 75, 1.75)
teste.emagrecer(10.00)
teste.envelhecer(2)
print(teste.envelhecer(2))
