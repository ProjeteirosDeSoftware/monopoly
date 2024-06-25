import pygame


class Faculdade:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
        self.imagem = pygame.image.load("./assets/carta_v.png")

    def mostra(self):
        font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        yield self.imagem
        yield font.render(self.nome, 1, (255, 255, 255))
