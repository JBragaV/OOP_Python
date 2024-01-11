from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):

    def __init__(self, nome: str, preco: float, tamanho: int):
        super().__init__(nome, preco)
        self._tamanho = f"{tamanho} ml"

    def __repr__(self):
        return f"{self._nome}"

    def aplicar_desconto(self):
        self._preco -= round(self._preco * 0.08, 2)
