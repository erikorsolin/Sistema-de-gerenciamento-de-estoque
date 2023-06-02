from model.produto import Produto
from view.tela_produto import TelaProduto
from random import randint
import json

class ControladorProduto:
    def __init__(self) -> None:
        self.tela_produto = TelaProduto()
        self.produtos = []
    

    def abre_tela(self) -> None:
        self.tela_produto.open()
    

    def adiciona(self) -> None:
        nome = self.tela_produto.pega_nome()
        cor = self.tela_produto.pega_cor()
        tamanho = self.tela_produto.pega_tamanho()
        preco = self.tela_produto.pega_preco()
        produto = Produto(randint(1000000, 999999999 ), nome, cor, tamanho, preco)
        self.produtos.append(produto)
        self.tela_produto.mostrar_mensagem("Produto cadastrado com sucesso!")
    

    def adiciona_em_JSON(self):
        for produto in self.produtos:
            id = produto.get_id()
            # Abre o arquivo no modo de leitura e escrita
            json_file = open('produto.json', 'r+')
            # Tenta ler o conteúdo do arquivo JSON existente
            try:
                dados = json.load(json_file)
            except json.decoder.JSONDecodeError:
            # Caso o arquivo esteja vazio ou inválido, inicializa com um dicionário vazio
                dados = {}

            produto = {"nome": produto.get_nome(), "cor": produto.get_cor(), "tamanho": produto.get_tamanho(), "preco": produto.get_preco()}
            dados[id] = produto  # Adiciona o novo produto ao dicionário

            # Retorna ao início do arquivo para sobrescrever o conteúdo antigo com o novo
            json_file.seek(0)
            # Escreve o dicionário completo no arquivo JSON
            json.dump(dados, json_file, indent=4)
            # Trunca o restante do arquivo, caso o novo conteúdo seja menor que o antigo
            json_file.truncate() 
            json_file.close() # Fecha o arquivo
        self.produtos = [] # Limpa a lista de produtos