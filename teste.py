from controller.controlador_produto import ControladorProduto
from model.produto import Produto

controlador = ControladorProduto()

controlador.produtos = [Produto(1, "Camiseta", "Branca", "M", 50.00), Produto(2, "Calça", "Azul", "M", 100.00), Produto(3, "Camiseta", "Preta", "G", 50.00), Produto(4, "Camiseta", "Branca", "P", 50.00), Produto(5, "Camiseta", "Branca", "G", 50.00), Produto(6, "Camiseta", "Branca", "GG", 50.00), Produto(7, "Camiseta", "Branca", "M", 50.00), Produto(8, "Camiseta", "Branca", "M", 50.00), Produto(9, "Camiseta", "Branca", "M", 50.00), Produto(10, "Camiseta", "Branca", "M", 50.00), Produto(11, "Camiseta", "Branca", "M", 50.00), Produto(12, "Camiseta", "Branca", "M", 50.00), Produto(13, "Camiseta", "Branca", "M", 50.00), Produto(14, "Camiseta", "Branca", "M", 50.00), Produto(15, "Camiseta", "Branca", "M", 50.00), Produto(16, "Camiseta", "Branca", "M", 50.00), Produto(17, "Camiseta", "Branca", "M", 50.00), Produto(18, "Camiseta", "Branca", "M", 50.00), Produto(19, "Camiseta", "Branca", "M", 50.00), Produto(20, "Camiseta", "Branca", "M", 50.00)] 
controlador.adiciona_em_JSON()

