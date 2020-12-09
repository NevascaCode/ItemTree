from Cores import Cores
import os
import pdb

def validar_escolha():
    while True:
        try:
            escolha = int(input("Escolha: "))
            break
        except:
            Cores("Por favor informe um número!").red()
    return escolha

espa = 1
sux = 0

class ItemTree(object):
    def __init__(self):
        self.lista_items = {'raiz': ['wood', 'iron'], 'wood': [], 'iron': ['ouro', 'dima', 'pegasus'], 'ouro': ['latao', 'QUEBRA'], 'dima': [], 'latao': ['lata', 'latinha'], 'QUEBRA': [], 'lata': ['cobra'], 'latinha': [], 'cobra': [], 'pegasus': []}
        self.item_pai = 'raiz'
        self.item_filho = ''
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
        print(self.lista_items)
        print(f"{'-=-'*10}-")

        self.criar_lista()

        self.item_pai = str(input('Item pai: '))
        if self.item_pai == '':
            self.item_pai = 'raiz'
        self.item_filho = str(input('item: '))

        self.adiciona_item(self.item_filho, self.item_pai)
        self.criar_arvore()

    def criar_lista(self):
        for item in self.lista_items["raiz"]:
            print(f'*{item}')
            self.verifica_filhos(item)

    def verifica_filhos(self, item):
        global espa
        global sux
        for dado in self.lista_items[item]:
            if dado == self.lista_items[item][-1]:
                print(f'{" "*espa}┗╸{dado}')
            else:
                print(f'{" "*espa}┣╸{dado}')
            espa+= 2
            if len(self.lista_items[item]) > 1:
                sux += 1
            self.verifica_filhos(dado)
            sux-=1
            espa-= 2

    def adiciona_item(self, filho, pai='raiz'):
        if pai in self.lista_items:
            self.lista_items[pai].append(filho)
        else:
            self.lista_items[pai] = [filho]

        if filho not in self.lista_items:
            self.lista_items[filho] = []


ItemTree()
