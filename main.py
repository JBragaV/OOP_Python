from modelos.restaurante import Restaurantes
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


rest1 = Restaurantes("Manolo", "Buteco")
bebida_breja = Bebida("Cerveja", 2.99, 500)
bebida_breja.aplicar_desconto()
prato_batata_frita_petisco = Prato("Batata Frita", 8.99, "Batata frita porção média para petiscar")
prato_batata_frita_petisco.aplicar_desconto()
rest1.alternar_estado()
rest1.receber_avaliaco("Jocimar", 222222222222222222222222222222222222222222)
rest1.receber_avaliaco("Cleiton", 5)
rest1.receber_avaliaco("Manuela", 4)


rest1.adicionar_item_ao_cardapio(prato_batata_frita_petisco)
rest1.adicionar_item_ao_cardapio(bebida_breja)
rest1.adicionar_item_ao_cardapio(rest1)

rest1.listar_cardapio()

rest2 = Restaurantes("Dominos", "Pizzaria", True)


rest3 = Restaurantes("Sushi do amor", "Japones", True)

# print(rest1)
# print(vars(rest2))
# print(rest3)
# Restaurantes.listar_restaurantes()
