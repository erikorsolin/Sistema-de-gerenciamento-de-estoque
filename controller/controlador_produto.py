from model.produto import Produto
from view.tela_produto import TelaProduto
import json

class ControladorProduto:
    def __init__(self) -> None:
        self.tela_produto = TelaProduto()
    


    def adiciona_produto(self):
        id = self.tela_produto.pega_id()
        nome = self.tela_produto.pega_nome()
        cor = self.tela_produto.pega_cor()
        tamanho = self.tela_produto.pega_tamanho()
        preco = self.tela_produto.pega_preco()
        # Abre o arquivo no modo de leitura e escrita
        json_file = open('produto.json', 'r+')
        # Tenta ler o conteúdo do arquivo JSON existente
        try:
            dados = json.load(json_file)
        except json.decoder.JSONDecodeError:
        # Caso o arquivo esteja vazio ou inválido, inicializa com um dicionário vazio
            dados = {}

        produto = {"nome": nome, "cor": cor, "tamanho": tamanho, "preco": preco}
        dados[id] = produto  # Adiciona o novo produto ao dicionário

        # Retorna ao início do arquivo para sobrescrever o conteúdo antigo com o novo
        json_file.seek(0)
        # Escreve o dicionário completo no arquivo JSON
        json.dump(dados, json_file, indent=4)
        # Trunca o restante do arquivo, caso o novo conteúdo seja menor que o antigo
        json_file.truncate() 
        json_file.close() # Fecha o arquivo
        self.tela_produto.mostra_mensagem("Produto cadastrado com sucesso!")
    



    def remove_produto(self) -> None:
        id = self.tela_produto.pega_id()
        # Abre o arquivo no modo de leitura e escrita
        json_file = open('produto.json', 'r+')
        # Tenta ler o conteúdo do arquivo JSON existente
        try:
            dados = json.load(json_file)
        except json.decoder.JSONDecodeError:
            # Caso o arquivo esteja vazio ou inválido, inicializa com um dicionário vazio
            dados = {}

        if id not in dados:
            self.tela_produto.mostra_mensagem("Produto não encontrado!")
            return
        # Remove o produto do dicionário
        dados.pop(str(id), None)
        # Retorna ao início do arquivo para sobrescrever o conteúdo antigo com o novo
        json_file.seek(0)
        # Escreve o dicionário completo no arquivo JSON
        json.dump(dados, json_file, indent=4)
        # Trunca o restante do arquivo, caso o novo conteúdo seja menor que o antigo
        json_file.truncate() 
        json_file.close()
        self.tela_produto.mostra_mensagem("Produto removido com sucesso!")



    
    def edita_produto(self) -> None:
        id = self.tela_produto.pega_id()
        cor = self.tela_produto.pega_cor()
        tamanho = self.tela_produto.pega_tamanho()
        preco = self.tela_produto.pega_preco()

        # Abre o arquivo no modo de leitura e escrita
        json_file = open('produto.json', 'r+')
        # Tenta ler o conteúdo do arquivo JSON existente
        try:
            dados = json.load(json_file)
        except json.decoder.JSONDecodeError:
            # Caso o arquivo esteja vazio ou inválido, inicializa com um dicionário vazio
            dados = {}

        if id not in dados:
            self.tela_produto.mostrar_mensagem("Produto não encontrado!")
            return
        # Edita o produto do dicionário
        dados[str(id)]["cor"] = cor
        dados[str(id)]["tamanho"] = tamanho
        dados[str(id)]["preco"] = preco
        # Retorna ao início do arquivo para sobrescrever o conteúdo antigo com o novo
        json_file.seek(0)
        # Escreve o dicionário completo no arquivo JSON
        json.dump(dados, json_file, indent=4)
        # Trunca o restante do arquivo, caso o novo conteúdo seja menor que o antigo
        json_file.truncate() 
        json_file.close()
        self.tela_produto.mostra_mensagem("Produto editado com sucesso!")



    def run(self):
        json_file = open('produto.json', 'r+')
        try:
            dados = json.load(json_file)
        except json.decoder.JSONDecodeError:
            dados = {}
        self.tela_produto.mostra_produtos(dados)
        json_file.close()
        self.tela_produto.iniciar()

        