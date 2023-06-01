from model.pessoa import Pessoa
from model.carrinho import Carrinho

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, senha: str):
        super().__init__(nome, cpf)
        self.senha = senha
        self.carrinho = Carrinho()
    
    def get_senha(self):
        return self.senha
    
    def set_senha(self, senha):
        self.senha = senha