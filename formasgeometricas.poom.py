import turtle

        # Classe base para todas as figuras
class Figura:
    def __init__(self, t, cor, tamanho, posicao):
        # Recebe o objeto turtle, cor, tamanho e posição da figura
        self.t = t
        self.cor = cor
        self.tamanho = tamanho
        self.posicao = posicao

    def desenhar(self):
        # Método genérico para desenhar a figura
        # Deve ser sobrescrito pelas subclasses
        pass
    def mover_para_posicao(self):
        # Move a tartaruga para a posição desejada sem desenhar
        self.t.penup()
        self.t.goto(self.posicao)
        self.t.pendown()
        self.t.color(self.cor) # Define a cor da caneta
        self.t.fillcolor(self.cor) # Define a cor do preenchimento
        self.t.begin_fill() # Inicia o preenchimento da figura

    def finalizar_desenho(self):
# Finaliza o preenchimento da figura
        self.t.end_fill()

# Subclasse para desenhar um triângulo
class Triangulo(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(3):
            self.t.forward(self.tamanho) # Desenha lado do triângulo
            self.t.left(120) # Gira 120 graus para formar o triângulo
        self.finalizar_desenho()

# Subclasse para desenhar um quadrado
class Quadrado(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(4):
            self.t.forward(self.tamanho) # Desenha lado do quadrado
             self.t.left(90)  # Gira 90 graus para formar o quadrado
        self.finalizar_desenho()

# Subclasse para desenhar um círculo
class Circulo(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        self.t.circle(self.tamanho) # Desenha o círculo com o raio informado
        self.finalizar_desenho()


# Subclasse para desenhar um hexágono
class Hexagono(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(6):
            self.t.forward(self.tamanho)  # Desenha lado do hexágono
            self.t.left(60)               # Gira 60 graus para formar o hexágono
        self.finalizar_desenho()

if __name__ == "__main__":
    # Configuração inicial da tela do turtle
    tela = turtle.Screen()
    tela.bgcolor("white")
    tela.title("Desenho POO com Turtle")

    # Cria o objeto turtle e define velocidade alta
    t = turtle.Turtle()
    t.speed(100)

    # Lista com as figuras a serem desenhadas, com cor, tamanho e posição
    figuras = [
        Triangulo(t, 'blue', 100, (0, 0)),
        Quadrado(t, 'yellow', 90, (100, -40)),
        Circulo(t, 'purple', 50, (0, 200)),
        Hexagono(t, 'red', 100, (-30, -200))
    ]

    # Desenha todas as figuras da lista
    for figura in figuras:
        figura.desenhar()
