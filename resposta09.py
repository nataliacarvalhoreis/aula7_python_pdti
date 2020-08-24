# Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
# A. Possua uma classe chamada Ponto, com os atributos x e y.
# B. Possua uma classe chamada Retangulo, com os atributos largura e altura.
# C. Possua uma função para imprimir os valores da classe Ponto
# D. Possua uma função para encontrar o centro de um Retângulo.
# E. Você deve criar alguns objetos da classe Retangulo.
# F. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do
# retângulo, que deve ser um objeto da classe Ponto.
# G. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do
# tipo ponto que indique os valores de x e y para o centro do objeto.
# H. O valor do centro do objeto deve ser mostrado na tela
# I. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimirPonto(self):
        print(f'x = {self.x} e y = {self.y}')


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centroRetangulo(self):
        centroX = self.largura//2
        centroY = self.altura//2
        centro = Ponto(centroX, centroY)
        return centro

    def verticePartida(self, x, y):
        p1 = Ponto(x, y)
        print("Vértice de Partida: ")
        p1.imprimirPonto()

    def alterarValores(self, x, y):
        self.largura = x
        self.altura = y

    def verRetangulo(self):
        print("Dados do Retângulo: ")
        print(f'Largura: {self.largura}')
        print(f'Altura: {self.altura}')

r1 = Retangulo(10, 20)
r1.verRetangulo()
r1.verticePartida(2, 15)

print("**MENU**")
print("1 - Alterar os valores do retângulo: ")
print("2 - Imprimir o centro do retângulo: ")

opcao = int(input("Informe a opção desejada: "))

if opcao == 1:
    largura = int(input("Informe a largura: "))
    altura = int(input("Informe a altura: "))
    r1.alterarValores(largura, altura)
elif opcao == 2:
    centroR1 = r1.centroRetangulo()
    print("O centro do Retângulo é: ")
    centroR1.imprimirPonto()
else:
    print("Opção inválida!")