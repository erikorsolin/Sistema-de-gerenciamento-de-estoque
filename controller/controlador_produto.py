import json

class ControladorProduto:
    @staticmethod
    def adiciona_produto(objeto) -> None:
        if objeto:
            # Abre o arquivo no modo de leitura e escrita
            json_file = open('produtos.json', 'r+')
            # Tenta ler o conteúdo do arquivo JSON existente
            try:
                dados = json.load(json_file)
            except json.decoder.JSONDecodeError:
            # Caso o arquivo esteja vazio ou inválido, inicializa com um dicionário vazio
                dados = {}
            id = objeto.get_id()
            produto = {"tipo": objeto.get_tipo(), "cor": objeto.get_cor(), "tamanho": objeto.get_tamanho(), "preco": objeto.get_preco(), "quantidade": objeto.get_quantidade()}
            dados[id] = produto  # Adiciona o novo produto ao dicionário

            # Retorna ao início do arquivo para sobrescrever o conteúdo antigo com o novo
            json_file.seek(0)
            # Escreve o dicionário completo no arquivo JSON
            json.dump(dados, json_file, indent=4)
            # Trunca o restante do arquivo, caso o novo conteúdo seja menor que o antigo
            json_file.truncate() 
            json_file.close() # Fecha o arquivo


    @staticmethod
    def remove_produto(id) -> None:
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


    @staticmethod
    def edita_produto(id, tipo, cor, tamanho, preco, quantidade) -> None:
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
        if tipo.isdigit() or tipo.isalpha():
            dados[str(id)]["tipo"] = tipo
        if cor.isalpha():
            dados[str(id)]["cor"] = cor
        if tamanho.isdigit() or tamanho.isalpha():
            dados[str(id)]["tamanho"] = tamanho
        if preco.isdigit():
            dados[str(id)]["preco"] = preco        
        if quantidade.isdigit():
            dados[str(id)]["quantidade"] = quantidade
        
        # Retorna ao início do arquivo para sobrescrever o conteúdo antigo com o novo
        json_file.seek(0)
        # Escreve o dicionário completo no arquivo JSON
        json.dump(dados, json_file, indent=4)
        # Trunca o restante do arquivo, caso o novo conteúdo seja menor que o antigo
        json_file.truncate() 
        json_file.close()


    @staticmethod
    def retornar_produtos() -> dict:  
        json_file = open('produtos.json', 'r+')
        try:
            dados = json.load(json_file)
        except json.decoder.JSONDecodeError:
            dados = {}
        json_file.close()

        return dados

        


        