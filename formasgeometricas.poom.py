import turtle

class Figura:
    def __init__(self, t, cor, tamanho, posicao):
        self.t = t
        self.cor = cor
        self.tamanho = tamanho
        self.posicao = posicao

    def desenhar(self):
        pass
    def mover_para_posicao(self):
        self.t.penup()
        self.t.goto(self.posicao)
        self.t.pendown()
        self.t.color(self.cor)
        self.t.fillcolor(self.cor)
        self.t.begin_fill()

    def finalizar_desenho(self):
        self.t.end_fill()

class Triangulo(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(3):
            self.t.forward(self.tamanho)
            self.t.left(120)
        self.finalizar_desenho()

class Quadrado(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(4):
            self.t.forward(self.tamanho)
            self.t.left(90)
        self.finalizar_desenho()

class Circulo(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        self.t.circle(self.tamanho)
        self.finalizar_desenho()

class Hexagono(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(6):
            self.t.forward(self.tamanho)
            self.t.left(60)
        self.finalizar_desenho()

if __name__ == "__main__":
    tela = turtle.Screen()
    tela.bgcolor("white")
    tela.title("Desenho POO com Turtle")

    t = turtle.Turtle()
    t.speed(100)

    figuras = [
        Triangulo(t, 'blue', 100, (0, 0)),
        Quadrado(t, 'yellow', 90, (100, -40)),
        Circulo(t, 'purple', 50, (0, 200)),
        Hexagono(t, 'red', 100, (-30, -200))
    ]

    for figura in figuras:
        figura.desenhar()

    turtle.done()
