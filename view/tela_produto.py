import tkinter as tk
from tkinter import ttk
import customtkinter

class TelaProduto:
    def __init__(self) -> None:
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.tela = customtkinter.CTk()
        self.tela.geometry("700x580")
        self.tela.title("Cadastro de Produtos")
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tela, width=500, height=300)
        self.scrollable_frame.place(x=95, y=240)
        
        self.button1 = customtkinter.CTkButton(self.tela, text="Adicionar Produto", width=150, corner_radius=6, command=None)
        self.button1.place(x=95, y=60)
        self.button2 = customtkinter.CTkButton(self.tela, text="Remover Produto", width=150, corner_radius=6, command=None)
        self.button2.place(x=95, y=100)
        self.button3 = customtkinter.CTkButton(self.tela, text="Editar Produto", width=150, corner_radius=6, command=None)
        self.button3.place(x=95, y=140)
        self.button4 = customtkinter.CTkButton(self.tela, text="Atualizar", width=150, corner_radius=6, command=None)
        self.button4.place(x=95, y=180)

        self.entry1 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="ID")
        self.entry1.place(x=450, y=20)
        self.entry2 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="TIPO")
        self.entry2.place(x=450, y=60)
        self.entry3 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="COR")
        self.entry3.place(x=450, y=100)
        self.entry4 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="TAMANHO")
        self.entry4.place(x=450, y=140)
        self.entry5 = customtkinter.CTkEntry(self.tela, width=150, corner_radius=6, placeholder_text="PREÇO")
        self.entry5.place(x=450, y=180)

    def mostra_produtos(self, produtos: dict) -> None:
        # Cabeçalho da tabela
        headers = ["ID", "TIPO", "COR", "TAMANHO", "PREÇO"]
        num_columns = len(headers)

        # Definir estilo dos rótulos com a cor de fundo do tema dark-blue
        style = ttk.Style()
        style.configure("DarkBlue.TLabel", background="#1e2531", foreground="white", font=("Arial", 12))

        # Criação dos rótulos do cabeçalho
        for i, header in enumerate(headers):
            label = ttk.Label(self.scrollable_frame, text=header, style="DarkBlue.TLabel")
            label.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")

        # Inserção dos produtos na tabela
        row = 1
        for id, produto in produtos.items():
            label_id = ttk.Label(self.scrollable_frame, text=id, style="DarkBlue.TLabel")
            label_id.grid(row=row, column=0, padx=10, pady=5, sticky="nsew")
            label_tipo = ttk.Label(self.scrollable_frame, text=produto.get("nome", ""), style="DarkBlue.TLabel")
            label_tipo.grid(row=row, column=1, padx=10, pady=5, sticky="nsew")
            label_cor = ttk.Label(self.scrollable_frame, text=produto.get("cor", ""), style="DarkBlue.TLabel")
            label_cor.grid(row=row, column=2, padx=10, pady=5, sticky="nsew")
            label_tamanho = ttk.Label(self.scrollable_frame, text=produto.get("tamanho", ""), style="DarkBlue.TLabel")
            label_tamanho.grid(row=row, column=3, padx=10, pady=5, sticky="nsew")
            label_preco = ttk.Label(self.scrollable_frame, text=produto.get("preco", ""), style="DarkBlue.TLabel")
            label_preco.grid(row=row, column=4, padx=10, pady=5, sticky="nsew")
            row += 1
        # Centralizar a tabela dentro do self.scrollable_frame
        for i in range(num_columns):
            self.scrollable_frame.grid_columnconfigure(i, weight=1)
        self.scrollable_frame.grid_rowconfigure(row, weight=1)

    
    def mostra_mensagem(self, mensagem: str) -> None:
        pass


    def iniciar(self):
        self.tela.mainloop()
    
    