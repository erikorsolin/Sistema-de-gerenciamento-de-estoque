class Produto:
    def __init__(self, id: int, tipo: str, cor: str, tamanho: str, preco: float, quantidade: int) -> None:
        self.id = str(id)
        self.tipo = tipo
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.quantidade = quantidade
    
    def get_id(self):
        return self.id
       
    def get_tipo(self):
        return self.tipo
    
    def get_cor(self):
        return self.cor
    
    def get_tamanho(self):
        return self.tamanho
    
    def get_preco(self):
        return self.preco
    
    def set_id(self, id):
        self.id = id
    
    def set_tipo(self, tipo):
        self.tipo = tipo
    
    def set_cor(self, cor):
        self.cor = cor
    
    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    def set_preco(self, preco):
        self.preco = preco
    
    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade