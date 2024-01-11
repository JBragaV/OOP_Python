from abc import ABC, abstractmethod


class ItemCardapio(ABC):

    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass
