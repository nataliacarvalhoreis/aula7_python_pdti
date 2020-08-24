# Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos
# nome e bucho (estomago) e pelo menos os métodos comer(), verBucho()
# e digerir(). Faça um programa ou teste interativamente, criando pelo
# menos dois macacos, alimentando-os com pelo menos 3 alimentos
# diferentes e verificando o conteúdo do estomago a cada refeição.
# Experimente fazer com que um macaco coma o outro. É possível criar um
# macaco canibal?

class Macaco:
    def __init__(self, nome, bucho = ""):
        self.nome = nome
        self.bucho = bucho

    def comer(self, alimento):
        if alimento != "":
            self.bucho = alimento


    def digerir(self):
        if(self.bucho != ""):
            self.bucho = ""
            return "Digerido!"
        else:
            return "Bucho Vazio!"

    def verBucho(self):
        print(f'Dentro do bucho do macaco {self.nome} tem {self.bucho}')

ole = Macaco("Ole")
pangole = Macaco("Pangole")

ole.comer("Folha")
ole.verBucho()
ole.comer("Banana")
ole.verBucho()
ole.comer("Ração")
ole.verBucho()
ole.digerir()
ole.verBucho()

pangole.comer("Folha")
pangole.verBucho()
pangole.comer("banana")
pangole.verBucho()
pangole.comer("farinha")
pangole.verBucho()
pangole.digerir()
pangole.verBucho()

ole.comer(pangole)
ole.verBucho()