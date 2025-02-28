# Sistema Bancário em Python 💳

Bem-vindo ao **Sistema Bancário em Python!** 💻 Este projeto é uma aplicação simples e eficiente que simula um sistema bancário, permitindo a criação de contas, depósitos, saques, e a visualização de extratos. O sistema é ideal para quem deseja aprender e aplicar conceitos de programação como manipulação de dicionários, controle de fluxo, e gerenciamento de dados em tempo real.

## 🚀 Funcionalidades

- **Cadastro de contas**: Crie contas bancárias com número e nome do titular.
- **Acesso às contas**: Realize login e interaja com a conta bancária do titular.
- **Depósitos**: Faça depósitos para aumentar o saldo da conta.
- **Saques com regras**: Limite de 3 saques diários, com valor máximo de R$ 500,00 por saque.
- **Extrato bancário**: Visualize todas as movimentações realizadas na conta ou uma mensagem caso não haja movimentações.
- **Controle de saques diários**: Controle rigoroso sobre os saques feitos durante o dia.

## 🧠 Habilidades Aplicadas

- **Python Básico e Avançado**: Uso de dicionários, listas e manipulação de dados.
- **Controle de Fluxo**: Utilização de condicionais (`if`, `else`) para controle de opções no menu.
- **Data e Hora**: Gerenciamento de data para limitar o número de saques diários.
- **Estrutura Modular**: Separação do código em módulos (`contas.py`, `operacoes.py`, `system.py`) para facilitar a organização e manutenção.
- **Funções e Regras de Negócio**: Implementação de regras como limites de saque, contagem de saques diários, e mensagens informativas.

## 🛠️ Tecnologias Usadas

- **Python 3.x**: Linguagem de programação utilizada para desenvolver o sistema.
- **datetime**: Biblioteca para gerenciar datas e controlar saques diários.
- **random**: Utilizada para gerar números aleatórios para os números das contas.

## 📥 Como Rodar o Projeto

1. Clone este repositório para sua máquina local:
   `git clone https://github.com/seu-usuario/sistema-bancario.git`

2. Acesse a pasta do projeto:
   `cd sistema-bancario`

3. Execute o arquivo principal:
   `python main.py`

4. Siga as instruções no terminal para interagir com o sistema.

## 📝 Exemplo de Execução

```
=== SISTEMA BANCÁRIO ===
1. Cadastrar conta
2. Acessar conta
3. Depositar
4. Sacar
5. Extrato
6. Sair da conta
7. Sair do sistema
Escolha uma opção: 1
Nome do titular: João Silva
Número da conta: 12345
Conta criada com sucesso para João Silva! Número da conta: 12345
...
```

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Se você tem alguma melhoria ou sugestão, fique à vontade para abrir uma issue ou enviar um **pull request**. Aqui estão algumas formas de contribuir:

1. Corrigir bugs e melhorar o código.
2. Adicionar novas funcionalidades.
3. Melhorar a documentação.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/GDEDevOne/sistema-bancario/blob/main/LICENSE) para mais detalhes.
