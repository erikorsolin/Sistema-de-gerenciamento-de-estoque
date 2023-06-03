import tkinter 

class TelaProduto:
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title("Produtos")
        self.root.geometry("600x500")
        self.root.mainloop()

    def mostra_opcoes(self) -> None:
        self.botao_adicionar = tkinter.Button(self.root, text="Adicionar", command=self.adiciona_produto)
        self.botao_adicionar.pack()
        self.botao_remover = tkinter.Button(self.root, text="Remover", command=self.remove_produto)
        self.botao_remover.pack()
        self.botao_editar = tkinter.Button(self.root, text="Editar", command=self.edita_produto)
        self.botao_editar.pack()

    def mostra_produtos_em_rolagem(self, dados: dict) -> None:
        pass

    def mostra_mensagem(self, mensagem: str) -> None:
        self.mensagem = tkinter.Label(self.root, text=mensagem)
        self.mensagem.pack()

            
    def pega_id(self) -> str:
        pass
    
    def pega_nome(self) -> str:
        pass
    
    def pega_cor(self) -> str:
        pass
    
    def pega_tamanho(self) -> str:
        pass
    
    def pega_preco(self) -> float:
        pass
    

    
