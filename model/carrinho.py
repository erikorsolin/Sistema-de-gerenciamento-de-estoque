class Carrinho:
    def __init__(self) -> None:
        self.produtos = list()
        self.preco_total = 0
        self.quantidade_produtos = 0

    def get_produtos(self):
        if self.produtos == []:
            return None
        return self.produtos
    
    def get_preco_total(self):
        return self.preco_total

    def get_quantidade_produtos(self):
        return self.quantidade_produtos 