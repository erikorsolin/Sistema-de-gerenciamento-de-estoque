import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

from view.tela_produto import TelaProduto

class TelaInicial:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.tela = customtkinter.CTk()
        self.tela.iconbitmap("view\images\logo.ico")
        self.tela.geometry("700x580")
        self.tela.title("Cadastro de Produtos")
        self.images()
        self.buttons()  


    def images(self):
        # Abrir a imagem usando PIL
        image = Image.open("view/images/store.png")

        # Redimensionar a imagem para o tamanho desejado
        width = 310  # Largura desejada
        height = 310  # Altura desejada
        image = image.resize((width, height), Image.ANTIALIAS)

        # Converter para um objeto PhotoImage
        logo = ImageTk.PhotoImage(image)

        # Criar o rótulo da imagem
        self.label_logo = tk.Label(self.tela, image=logo)
        self.label_logo.place(x=290, y=50)

        # Configurar a cor de fundo do rótulo para corresponder à cor de fundo da janela
        self.label_logo.configure(bg=self.tela["bg"])

        # Definir a cor do pixel no canto superior esquerdo como transparência
        self.label_logo.image = logo  # Manter uma referência à imagem para evitar a coleta de lixo
        self.label_logo["highlightthickness"] = 0



    def buttons(self):
        self.btn = customtkinter.CTkButton(self.tela, text="Iniciar", command=self.iniciar_tela_produtos)
        self.btn.place(x=285, y=385)


    def iniciar_tela_produtos(self):
        self.tela.destroy()
        tela_produto = TelaProduto()
        tela_produto.iniciar()


    def mostra_tela(self):
        self.tela.mainloop()