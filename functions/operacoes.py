from . import contas
import datetime

def realizar_deposito(valor):
    """Realiza um depósito na conta atual."""
    if not contas.conta_atual:
        print("Nenhuma conta logada. Faça login primeiro.")
        return
    
    if valor <= 0:
        print("O valor do depósito deve ser positivo.")
        return
    
    conta = contas.banco[contas.conta_atual]
    conta["saldo"] += valor
    conta["movimentacoes"].append({"tipo": "depósito", "valor": valor})

    print(f"Depósito de R$ {valor:.2f} realizado para {contas.conta_atual}.")

def realizar_saque(valor):
    """Realiza um saque da conta atual."""

    if not contas.conta_atual:
        print("Nenhuma conta logada. Faça login primeiro.")
        return
    
    conta = contas.banco[contas.conta_atual]
    hoje = datetime.date.today()

    # Verifica se o último saque foi no mesmo dia
    if conta["ultimo_saque"] == hoje:
        if conta["saques_diarios"] >= 3:
            print(f"Você já fez 3 saques hoje. Limite diário atingido.")
            return
    else:
        # Resetar o contador de saques no novo dia
        conta["saques_diarios"] = 0
        conta["ultimo_saque"] = hoje

    if valor > 500:
        print("O valor do saque não pode ultrapassar R$ 500,00.")
        return

    if valor <= 0:
        print("O valor do saque deve ser positivo.")
        return
    
    if conta["saldo"] >= valor:
        conta["saldo"] -= valor
        conta["saques_diarios"] += 1
        conta["movimentacoes"].append({"tipo": "saque", "valor": valor})

        print(f"Saque de R$ {valor:.2f} realizado para {contas.conta_atual}.")
    else:
        print("Saldo insuficiente!")

def exibir_extrato():
    """Exibe o extrato de movimentações da conta atual."""

    if not contas.conta_atual:
        print("Nenhuma conta logada. Faça login primeiro.")
        return
    
    conta = contas.banco[contas.conta_atual]

    if not conta["movimentacoes"]:
        print("Não foram realizadas movimentações.")
        return

    print("\n=== EXTRATO ===")
    for mov in conta["movimentacoes"]:
        print(f"{mov['tipo'].capitalize()} de R$ {mov['valor']:.2f}")

    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")