from typing import List, Tuple
import pygame

from faculdade import Faculdade


class Janela:
    def calcula_janela(self, base: int, dimensao: Tuple[int, int]):
        return (dimensao[0]*base, dimensao[1]*base)

    def __init__(
        self,
        base=50,
        dimensao=(10, 10)
    ):
        self.items: List[Faculdade] = []
        self.janela = pygame.display.set_mode(self.calcula_janela(base, dimensao))
        self.janela.fill((0, 0, 0))

    def adiciona_elemento(self, elemento):
        self.items.append(elemento)

    def mostra(self):
        pygame.display.flip()

        for item in self.items:
            for elemento in item.mostra():
                self.janela.blit(elemento, item.posicao)

        pygame.display.update()
