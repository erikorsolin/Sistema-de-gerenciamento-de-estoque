class SistemaVendas:
    def __init__(self):
        self.produtos = []
        self.clientes = []

    def get_produtos(self):
        return self.produtos
    
    def get_clientes(self):
        return self.clientes
    
    def set_produtos(self, produtos):
        self.produtos = produtos

    def set_clientes(self, clientes):
        self.clientes = clientes
    
    