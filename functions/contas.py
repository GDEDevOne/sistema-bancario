import random
import datetime
import re

class Banco:
    def __init__(self):
        self.banco = {}
        self.conta_atual = None
        self.numeros_de_conta_usados = set()
        self.cpfs_cadastrados = set()

    def gerar_numero_conta(self):
        """Gera um número de conta único e não repetido."""

        while True:
            numero = random.randint(10000, 99999)
            if numero not in self.numeros_de_conta_usados:
                self.numeros_de_conta_usados.add(numero)
                
                return numero

    def validar_cpf(self, cpf):
        """Valida se o endereço está no formato correto."""
        if not re.fullmatch(r'\d{11}', cpf):
            print("Erro: CPF inválido! Deve conter exatamente 11 números.")
            return False
        
        if cpf in self.cpfs_cadastrados:
            print("Erro: CPF já cadastrado!")
            return False

        return True

    def validar_endereco(self, endereco):
        """Valida se o endereço está no formato correto."""

        return re.fullmatch(r'.+, \d+ - .+ - .+/[A-Z]{2}', endereco)

    def cadastrar_conta(self):
        """Cadastra uma nova conta para o titular fornecido."""

        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
        cpf = input("CPF (somente números): ")
        endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")

        if self.validar_cpf(cpf) == False:
            print("CPF inválido ou já cadastrado.")
            return
        
        if not self.validar_endereco(endereco):
            print("Endereço em formato inválido.")
            return
        
        numero_conta = self.gerar_numero_conta()
        numero_agencia = "0001"

        self.banco[cpf] = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
            "conta": numero_conta, 
            "agencia": numero_agencia,
            "saldo": 0.0, 
            "movimentacoes": [], 
            "saques_diarios": 0, 
            "ultimo_saque": None
        }

        self.cpfs_cadastrados.add(cpf)

        print(f"Conta criada com sucesso para {nome}! Número da agência: {numero_agencia}, Conta: {numero_conta}")

    def acessar_conta(self):
        """Acessa a conta de um titular pelo CPF."""

        cpf = input("Digite o CPF: ")

        if cpf in self.banco:
            self.conta_atual = cpf
            print(f"Conta de {self.banco[cpf]['nome']} (Agência {self.banco[cpf]['agencia']}, Conta {self.banco[cpf]['conta']}) acessada com sucesso!")
        else:
            print("Conta não encontrada.")

    def sair_conta(self):
        """Desfaz o login da conta atual."""
        
        if self.conta_atual:
            print(f"Saindo da conta de {self.banco[self.conta_atual]['nome']}.")
            self.conta_atual = None
        else:
            print("Nenhuma conta logada.")