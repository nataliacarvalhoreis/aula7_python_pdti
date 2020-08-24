# Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos
# nome e bucho (estomago) e pelo menos os métodos comer(), verBucho()
# e digerir(). Faça um programa ou teste interativamente, criando pelo
# menos dois macacos, alimentando-os com pelo menos 3 alimentos
# diferentes e verificando o conteúdo do estomago a cada refeição.
# Experimente fazer com que um macaco coma o outro. É possível criar um
# macaco canibal?
import random
import time

class macaco:
    def __init__(self, nome, bucho=['']):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)
        print("Comer.", self.nome)
        return

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []

    def mostra(self):
        return self.nome

comidas = ['banana','melão','laranja','mamão','maçã','uva']
jose = macaco('jose')
joao = macaco('joao')

while True:
    print(f"Como estão os macacos")
    print(f"1 {jose.mostra()}, tem no bucho: {jose.verBucho()}")
    print(f"2 {joao.mostra()}, tem no bucho: {joao.verBucho()}")
    time.sleep(1)

    sorteia = random.randint(1, 5)

    if sorteia == 1:  # hora de comer para xita
        jose.comer(comidas[random.randint(0, len(comidas) - 1)])
    elif sorteia == 2:  # hora de comer para banze
        joao.comer(comidas[random.randint(0, len(comidas) - 1)])
    elif sorteia == 3:  # hora de digestão para xita
        jose.digerir()
    elif sorteia == 4:  # hora de digestão para banze
        joao.digerir()