# Sistema de venda de roupas
![image](https://github.com/erikorsolin/Sistema-de-venda-de-roupas/assets/107228254/6cc5f81e-3580-4d0e-9ea6-f236fe88df71)

Este é um projeto referente à AA4 (Atividade Avaliativa 4) da disciplina INE5404 (Programação Orientada a Objetos II) da UFSC.
O sistema de vendas de roupas foi desenvolvido em Python utilizando o padrão de projeto MVC (Model View Controller). O sistema permite realizar as operações CRUD (create, retrieve, update, delete) para o gerenciamento do estoque de roupas de uma loja. A interface gráfica moderna é desenvolvida com a biblioteca customtkinter e a persistência de dados é feita utilizando arquivos JSON.

## Funcionalidades
+ Criação de novos itens de estoque, incluindo informações como ID, tipo, cor, tamanho, preço.
+ Visualização dos itens de estoque existentes.
+ Atualização das informações de um item de estoque específico.
+ Remoção de um item de estoque existente.

## Pré-Requisitos
Para executar o sistema de vendas de roupas, você precisa ter as seguintes bibliotecas instaladas:
+ `tkinter`: Biblioteca padrão do Python para criar interfaces gráficas.
+ `customtkinter`: Biblioteca customizada para aprimorar a interface gráfica do sistema.

 Você pode instalar as bibliotecas utilizando o gerenciador de pacotes pip. Execute o seguinte comando:
 ```
 pip install tkinter customtkinter
 ```
 
 ## Como executar o sistema
 1. Clone este repositório para o seu ambiente local:
 ```
 git clone https://github.com/erikorsolin/Sistema-de-venda-de-roupas.git
 ```
 
 2. Navegue até o diretório do projeto:
  ```
 cd Sistema-de-venda-de-roupas
 ```
 
 3. Execute o arquivo principal do sistema:
 ```
 python main.py
 ```
 
 ## Estrutura do Projeto
 O projeto segue uma estrutura organizada, separando as responsabilidades em diferentes módulos:
 + `model`: Contém a definição do modelo de dados
 + `view`: Responsável por criar a interface gráfica e interagir com o usuário
 + `controller`: Gerencia as ações do usuário e conecta a interface gráfica com a lógica de negócios (leitura e gravação no arquivo JSON)


## Contribuindo
Contribuições são bem-vindas! Se você quiser melhorar o sistema de vendas de roupas, sinta-se à vontade para enviar pull requests. Antes de fazer qualquer alteração significativa, abra uma issue para discutir a proposta.
