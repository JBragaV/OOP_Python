from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):

    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __repr__(self):
        return f"{self._nome}"

    def aplicar_desconto(self):
        self._preco -= round((self._preco * 0.06), 2)
