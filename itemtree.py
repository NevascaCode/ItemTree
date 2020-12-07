from Cores import Cores
import os
def validar_escolha():
    while True:
        try:
            escolha = int(input("Escolha: "))
            break
        except:
            Cores("Por favor informe um número!").red()
    return escolha

class ItemTree(object):
    def __init__(self):
        self.lista_items = {}
        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        print(f"{'-=-='*10}-")
        print(f"{'Bem Vindo ao Item-Tree':^41}")
        print(f"{'-=-='*10}-")

        print("1 - Criar uma Arvore de Item",
              "\n2 - Executar uma Arvore de Item",
              "\n3 - Sair")

        escolha = validar_escolha()
        while escolha not in [1, 2, 3]:
            Cores("Por favor escolha entre as opeções!").red()
            escolha = validar_escolha()

        if escolha == 1:
            self.nome_da_arvore = str(input("Nome da Arvore: "))
            self.criar_arvore()
        elif escolha ==2:
            print('Em Breve')
        else:
            print('Obrigado por testar!!!')

    def criar_arvore(self):
        os.system("cls")
        print(f"{'-=-'*10}-")
        print(f"{self.nome_da_arvore:^31}")
        print(f"{'-=-'*10}-")


ItemTree()
