from random import randint
from typing import Tuple

class Dados:
    def __init__(self):
        pass

    def rolarDados(self) -> Tuple[int, int]:
        return randint(1, 6), randint(1, 6)
