import functions.contas as contas
import functions.operacoes as operacoes

def exibir_menu():
    """Exibe o menu principal do sistema bancário."""

    print("\n=== SISTEMA BANCÁRIO ===")
    print("1. Cadastrar conta")
    print("2. Acessar conta")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Extrato")
    print("6. Sair da conta")
    print("7. Sair do sistema")

def obter_opcao_usuario():
    """Obtém a opção escolhida pelo usuário e valida a entrada."""

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))

            if 1 <= opcao <= 7:
                return opcao
            else:
                print("Opção inválida. Por favor, escolha um número entre 1 e 7.")

        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def executar_opcao(opcao):
    """Executa a ação correspondente à opção escolhida pelo usuário."""

    if opcao == 1:
        nome = input("Nome do titular: ")
        contas.cadastrar_conta(nome)

    elif opcao == 2:
        nome = input("Nome do titular: ")
        contas.acessar_conta(nome)

    elif opcao == 3:
        try:
            valor = float(input("Valor do depósito: "))
            operacoes.realizar_deposito(valor)
        except ValueError:
            print("Valor inválido. Tente novamente.")

    elif opcao == 4:
        try:
            valor = float(input("Valor do saque: "))
            operacoes.realizar_saque(valor)
        except ValueError:
            print("Valor inválido. Tente novamente.")

    elif opcao == 5:
        operacoes.exibir_extrato()

    elif opcao == 6:
        contas.sair_conta()

    elif opcao == 7:
        print("Encerrando o sistema...")

        return False
    return True

def run():
    """Função principal para execução do sistema bancário."""
    
    while True:
        exibir_menu()
        opcao = obter_opcao_usuario()
        if not executar_opcao(opcao):
            break