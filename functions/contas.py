import random
import datetime

banco = {}
conta_atual = None
numeros_de_conta_usados = set()

def gerar_numero_conta():
    """Gera um número de conta único e não repetido."""

    while True:
        numero = random.randint(10000, 99999)
        if numero not in numeros_de_conta_usados:
            numeros_de_conta_usados.add(numero)
            
            return numero

def cadastrar_conta(nome):
    """Cadastra uma nova conta para o titular fornecido."""

    if nome in banco:
        print(f"Já existe uma conta cadastrada para {nome}.")
        return
    
    numero_conta = gerar_numero_conta()
    banco[nome] = {
        "conta": numero_conta, 
        "saldo": 0.0, 
        "movimentacoes": [], 
        "saques_diarios": 0, 
        "ultimo_saque": None
    }

    print(f"Conta criada com sucesso para {nome}! Número da agência: {numero_conta}")

def acessar_conta(nome):
    """Acessa a conta de um titular pelo nome."""

    global conta_atual

    if nome in banco:
        conta_atual = nome

        print(f"Conta de {nome} (Agência {banco[nome]['conta']}) acessada com sucesso!")
    else:
        print("Conta não encontrada.")

def sair_conta():
    """Desfaz o login da conta atual."""

    global conta_atual
    
    if conta_atual:
        print(f"Saindo da conta de {conta_atual}.")
        conta_atual = None
    else:
        print("Nenhuma conta logada.")