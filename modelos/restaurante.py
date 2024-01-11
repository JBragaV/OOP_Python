from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurantes:

    restaurantes = []

    def __init__(self, nome: str, categoria: str, ativo=False):
        self._nome = nome
        self._categoria = categoria
        self._ativo = ativo
        self._avaliacoes = []
        self._cardapio = []
        Restaurantes.restaurantes.append(self)

    @property
    def ativo(self) -> str:
        """Essa property é comparável aos métodos get de outras linguagens de programação"""
        return "Ativo" if self._ativo else "Desativado"

    def __repr__(self):
        return f"O restaurante {self._nome} é da categoria {self._categoria} e está {self.ativo} no sistema"

    def alternar_estado(self) -> None:
        self._ativo = not self._ativo

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)} | Status")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | "
                  f"{str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    def receber_avaliaco(self, cliente: str, nota: float) -> None:
        if nota > 5:
            nota = 5
        elif nota < 0:
            nota = 0
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self) -> str | float:
        if not self._avaliacoes:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        return round(soma_das_notas/quantidade_de_notas, 1)

    def adicionar_item_ao_cardapio(self, item: ItemCardapio) -> None:
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def listar_cardapio(self):
        print(f"Cardapio do Restaurante {self._nome}\n")
        for id, item in enumerate(self._cardapio, 1):
            if hasattr(item, "_descricao"):
                print(f"{id}. {str(item._nome).ljust(20)} | R${str(item._preco).ljust(20)} "
                      f"| Descição: {item._descricao}")
            elif hasattr(item, "_tamanho"):
                print(f"{id}. {str(item._nome).ljust(20)} | R${str(item._preco).ljust(20)} "
                      f"| Tamanho: {item._tamanho}")

