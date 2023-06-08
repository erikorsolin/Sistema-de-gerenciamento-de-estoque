import tkinter as tk
from tkinter import ttk
import customtkinter
from controller.controlador_produto import ControladorProduto

class TelaProduto():
    def __init__(self) -> None:
        self.tela = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.tela.iconbitmap("view\images\logo.ico")
        self.tela.geometry("700x580")
        self.tela.title("Cadastro de Produtos")
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tela, width=500, height=300)
        self.scrollable_frame.place(x=95, y=240)      
        self.buttons()
        self.entrys()


    def mostra_produtos(self) -> None:
        # Cabeçalho da tabela
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        produtos = ControladorProduto.retornar_produtos()
        headers = ["ID", "TIPO", "COR", "TAMANHO", "PREÇO", "QUANTIDADE"]
        num_columns = len(headers)

        # Definir estilo dos rótulos com a cor de fundo do tema dark-blue
        style = ttk.Style()
        style.configure("DarkBlue.TLabel", background="#1e2531", foreground="white", font=("Arial", 13))

        # Criação dos rótulos do cabeçalho
        for i, header in enumerate(headers):
            label = ttk.Label(self.scrollable_frame, text=header, style="DarkBlue.TLabel")
            label.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")

        # Inserção dos produtos na tabela
        row = 1
        for id, produto in produtos.items():
            label_id = ttk.Label(self.scrollable_frame, text=id, style="DarkBlue.TLabel")
            label_id.grid(row=row, column=0, padx=10, pady=5, sticky="nsew")
            label_tipo = ttk.Label(self.scrollable_frame, text=produto.get("tipo", ""), style="DarkBlue.TLabel")
            label_tipo.grid(row=row, column=1, padx=10, pady=5, sticky="nsew")
            label_cor = ttk.Label(self.scrollable_frame, text=produto.get("cor", ""), style="DarkBlue.TLabel")
            label_cor.grid(row=row, column=2, padx=10, pady=5, sticky="nsew")
            label_tamanho = ttk.Label(self.scrollable_frame, text=produto.get("tamanho", ""), style="DarkBlue.TLabel")
            label_tamanho.grid(row=row, column=3, padx=10, pady=5, sticky="nsew")
            label_preco = ttk.Label(self.scrollable_frame, text=produto.get("preco", ""), style="DarkBlue.TLabel")
            label_preco.grid(row=row, column=4, padx=10, pady=5, sticky="nsew")
            label_quantidade = ttk.Label(self.scrollable_frame, text=produto.get("quantidade", ""), style="DarkBlue.TLabel")
            label_quantidade.grid(row=row, column=5, padx=10, pady=5, sticky="nsew")
            row += 1
        # Centralizar a tabela dentro do self.scrollable_frame
        for i in range(num_columns):
            self.scrollable_frame.grid_columnconfigure(i, weight=1)
        self.scrollable_frame.grid_rowconfigure(row, weight=1)

    
    def entrys(self) -> None:
        self.entry1 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="ID")
        self.entry1.place(x=350, y=60)
        self.entry2 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="TIPO")
        self.entry2.place(x=350, y=100)
        self.entry3 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="COR")
        self.entry3.place(x=350, y=140)
        self.entry4 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="TAMANHO")
        self.entry4.place(x=520, y=60)
        self.entry5 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="PREÇO")
        self.entry5.place(x=520, y=100)
        self.entry6 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="QUANTIDADE")
        self.entry6.place(x=520, y=140)
    

    def buttons(self) -> None:
        self.button1 = customtkinter.CTkButton(self.tela, text="Adicionar Produto", width=150, corner_radius=6,  command=lambda: ControladorProduto.adiciona_produto(self.pega_id(), self.pega_tipo(), self.pega_cor(), self.pega_tamanho(), self.pega_preco(), self.pega_quantidade()))
        self.button1.place(x=95, y=60)
        self.button2 = customtkinter.CTkButton(self.tela, text="Remover Produto", width=150, corner_radius=6,  command=lambda: ControladorProduto.remove_produto(self.pega_id()))
        self.button2.place(x=95, y=100)
        self.button3 = customtkinter.CTkButton(self.tela, text="Editar Produto", width=150, corner_radius=6,  command=lambda: ControladorProduto.edita_produto(self.pega_id(), self.pega_tipo(), self.pega_cor(), self.pega_tamanho(), self.pega_preco(), self.pega_quantidade()))
        self.button3.place(x=95, y=140)
        self.button4 = customtkinter.CTkButton(self.tela, text="Atualizar", width=150, corner_radius=6,  command=self.iniciar)
        self.button4.place(x=95, y=180)
    

    def pega_id(self) -> str:
        return self.entry1.get().upper()
    
    def pega_tipo(self) -> str:
        return self.entry2.get().upper()
    
    def pega_cor(self) -> str:
        return self.entry3.get().upper()
    
    def pega_tamanho(self) -> str:
        return self.entry4.get().upper()

    def pega_preco(self) -> str:
        return self.entry5.get()

    def pega_quantidade(self) -> int:
        return self.entry6.get()
    
    def atualiza_tela(self) -> None:
        # Mostra os produtos atualizados
        self.mostra_produtos()

    def iniciar(self):
        self.mostra_produtos()
        self.tela.mainloop()
    
    