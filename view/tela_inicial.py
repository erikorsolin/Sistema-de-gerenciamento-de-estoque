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
        self.entrys()
        self.__senha = "adm1234"


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
    
    def entrys(self):
        self.senha = customtkinter.CTkEntry(self.tela, show="*", placeholder_text="Senha")
        self.senha.place(x=285, y=340)

    def labels(self):
        self.label = customtkinter.CTkLabel(self.tela, text="")
        self.label.place(x=285, y=340)

    def pega_senha(self):
        return self.senha.get()
        

    def iniciar_tela_produtos(self):
        if self.pega_senha() == self.__senha:
            self.tela.destroy()
            tela_produto = TelaProduto()
            tela_produto.iniciar()
        else:
            self.label = customtkinter.CTkLabel(self.tela, text="Senha incorreta")
            self.label.place(x=305, y=420)
            self.label.after(2000, self.label.destroy)


    def mostra_tela(self):
        self.tela.mainloop()