import pygame as pg
from faculdade import Faculdade
from janela import Janela


class Jogo:
    def __init__(self):
        pg.init()
        self.janela = Janela()

    def game_loop(self):
        sair = False

        fac = [Faculdade("faculdade", (0, 0))]
        for f in fac:
            self.janela.adiciona_elemento(f)
        while not sair:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sair = True

            self.janela.mostra()
