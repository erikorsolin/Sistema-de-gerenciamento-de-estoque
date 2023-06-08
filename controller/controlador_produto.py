from model.produto import Produto
import json

class ControladorProduto:
    def __init__(self):
        pass

    def adiciona_produto(self, id, tipo, cor, tamanho, preco, quantidade) -> None:
        # Abre o arquivo no modo de leitura e escrita
        json_file = open('produtos.json', 'r+')
        # Tenta ler o conteúdo do arquivo JSON existente
        try:
            dados = json.load(json_file)
        except json.decoder.JSONDecodeError:
        # Caso o arquivo esteja vazio ou inválido, inicializa com um dicionário vazio
            dados = {}

        produto = {"tipo": tipo, "cor": cor, "tamanho": tamanho, "preco": preco, "quantidade": quantidade}
        dados[id] = produto  # Adiciona o novo produto ao dicionário

        # Retorna ao início do arquivo para sobrescrever o conteúdo antigo com o novo
        json_file.seek(0)
        # Escreve o dicionário completo no arquivo JSON
        json.dump(dados, json_file, indent=4)
        # Trunca o restante do arquivo, caso o novo conteúdo seja menor que o antigo
        json_file.truncate() 
        json_file.close() # Fecha o arquivo
    



    def remove_produto(self, id) -> None:
        # Abre o arquivo no modo de leitura e escrita
        json_file = open('produtos.json', 'r+')
        # Tenta ler o conteúdo do arquivo JSON existente
        try:
            dados = json.load(json_file)
        except json.decoder.JSONDecodeError:
            # Caso o arquivo esteja vazio ou inválido, inicializa com um dicionário vazio
            dados = {}

        if id not in dados:
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


    
    def edita_produto(self, id, tipo, cor, tamanho, preco, quantidade) -> None:
        # Abre o arquivo no modo de leitura e escrita
        json_file = open('produtos.json', 'r+')
        # Tenta ler o conteúdo do arquivo JSON existente
        try:
            dados = json.load(json_file)
        except json.decoder.JSONDecodeError:
            # Caso o arquivo esteja vazio ou inválido, inicializa com um dicionário vazio
            dados = {}

        if id not in dados:
            return
        # Edita o produto do dicionário
        dados[str(id)]["tipo"] = tipo
        dados[str(id)]["cor"] = cor
        dados[str(id)]["tamanho"] = tamanho
        dados[str(id)]["preco"] = preco
        dados[str(id)]["quantidade"] = quantidade
        # Retorna ao início do arquivo para sobrescrever o conteúdo antigo com o novo
        json_file.seek(0)
        # Escreve o dicionário completo no arquivo JSON
        json.dump(dados, json_file, indent=4)
        # Trunca o restante do arquivo, caso o novo conteúdo seja menor que o antigo
        json_file.truncate() 
        json_file.close()



    def retornar_produtos(self):  
        json_file = open('produtos.json', 'r+')
        try:
            dados = json.load(json_file)
        except json.decoder.JSONDecodeError:
            dados = {}
        json_file.close()

        return dados

        


        