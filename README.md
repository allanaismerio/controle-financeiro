Sobre o Projeto

O Controle Financeiro é uma aplicação simples desenvolvida para ajudar o usuário a gerenciar entradas e saídas de dinheiro de forma prática e organizada.
O sistema permite registrar transações, classificar como entrada ou saída, salvar automaticamente no navegador (localStorage) e visualizar o saldo atualizado em tempo real.

Este projeto pode ser utilizado como base para estudos, portfólio ou expansão para um sistema financeiro completo.

 Funcionalidades

Adicionar transações com:

Descrição

Valor

Tipo (Entrada / Saída)

Exibição automática da lista de transações

Cálculo do saldo total

Armazenamento local usando localStorage

Remoção de transações

Interface simples e objetiva

 Estrutura de Pastas do Projeto
controle_financeiro/
│── index.html
│── style.css
│── script.js
└── README.md

 index.html

Contém a estrutura básica da interface com o formulário e a lista de transações.

 style.css

Responsável pelo visual do sistema: cores, layout e responsividade simples.

 script.js

Toda a lógica da aplicação está aqui:

gerenciamento de transações

cálculos

interação com localStorage

 Como Executar o Projeto

Baixe ou clone este repositório:

git clone https://github.com/seu-usuario/controle_financeiro.git


Abra o arquivo index.html no navegador:

Dê dois cliques
ou

Execute com uma extensão live server (VSCode, por exemplo)

Não há necessidade de instalar dependências — o projeto é totalmente em HTML + CSS + JavaScript puro.

 Como Funciona o Sistema
➤ Salvando Transações

Cada transação criada é registrada como um objeto:

{
  id: 1,
  descricao: "Salário",
  valor: 2000,
  tipo: "entrada"
}


Todas ficam armazenadas no localStorage, garantindo que persistam mesmo após fechar o navegador.

➤ Calculando o Saldo

O sistema soma os valores das entradas e subtrai as saídas:

saldo = soma(entradas) – soma(saídas)

 Melhorias Futuras (Sugestões)

Se quiser evoluir o projeto, aqui vão ideias:

Filtrar transações por data

Filtro por tipo (entradas/saídas)

Categorias: alimentação, transporte, lazer etc.

Exportar relatório em PDF ou CSV

Login com autenticação

Dashboard com gráficos (Chart.js)

API backend com banco de dados

Posso adicionar qualquer uma dessas melhorias para você!

 Tecnologias Utilizadas

HTML5

CSS3

JavaScript (ES6+)

LocalStorage

 Autor

Desenvolvido por Allana Ismério
