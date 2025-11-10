# Controle Financeiro Pessoal com FastAPI

Este é um projeto de aplicação web para gerenciamento de finanças pessoais. Ele permite ao usuário adicionar receitas e despesas, que são listadas em uma tabela, e exibe o saldo total atualizado em tempo real.

A aplicação é construída inteiramente em **Python** usando o framework **FastAPI** para o back-end, **SQLAlchemy** para o banco de dados e **Jinja2** para renderizar o front-end em HTML/CSS.

## Funcionalidades

* **Adicionar Transações:** Formulário para adicionar novas entradas, especificando se é 'Receita' ou 'Despesa'.
* **Listar Transações:** Todas as transações são exibidas em uma tabela.
* **Cálculo de Saldo:** O saldo total é calculado (Receitas - Despesas) e exibido no topo da página.
* **Excluir Transações:** É possível remover transações individualmente.
* **Persistência de Dados:** Os dados são salvos em um banco de dados SQLite.

## Tecnologias Utilizadas

* **Back-end:**
    * **Python 3**
    * **FastAPI:** Framework web para a criação da API.
    * **Uvicorn:** Servidor ASGI para executar a aplicação.
* **Banco de Dados:**
    * **SQLAlchemy (ORM):** Para interagir com o banco de dados usando Python.
    * **SQLite:** Banco de dados relacional baseado em arquivo.
* **Front-end:**
    * **Jinja2:** Motor de templates para injetar dados do Python no HTML.
    * **HTML5:** Para a estrutura da página.
    * **CSS3:** Para a estilização.

## Estrutura do Projeto
/ ├── static/ 
│ └── style.css # Folha de estilos 
├── templates/ 
│ └── index.html # Template HTML com Jinja2 
├── .gitignore # Ignora arquivos (como o .db) 
├── database.py # Configuração da conexão com o banco (SQLAlchemy) 
├── main.py # Lógica principal da aplicação (rotas FastAPI) 
├── models.py # Definição das tabelas do banco (Modelo SQLAlchemy) 
├── procfile.txt # (Opcional) Para deploy no Heroku 
└── requirements.txt # Lista de dependências Python


## ⚙️ Como Executar Localmente

Você precisará ter o Python 3 instalado.

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```sh
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Execute o servidor:**
    ```sh
    uvicorn main:app --reload
    ```
    * `--reload` faz o servidor reiniciar automaticamente a cada mudança no código.

5.  **Acesse no navegador:**
    Abra seu navegador e visite `http://127.0.0.1:8000`
