'''ItemTree'''

from Cores import Cores
from time import sleep
import os


def validar_escolha(lista_escolha=[]):
    '''Valida Escolha'''
    while True:
        try:
            Cores.limpador()
            escolha = int(input(f"┣ Escolha: {Cores.amarelo}"))
            Cores.limpador()
            if escolha not in lista_escolha:
                print(f"{Cores.vermelho}┃Por favor escolha entre as opeções!")
            else:
                break
        except ValueError:
            Cores.limpador()
            print(f"{Cores.vermelho}┃Por favor informe um número!")
    return escolha

class ItemTree(object):
    def __init__(self):
        self.lista_items = {'raiz': ['wood', 'iron'], 'wood': [], 'iron': ['ouro', 'dima', 'pegasus'], 'ouro': ['latao', 'QUEBRA'], 'dima': [], 'latao': ['lata', 'latinha', 'quebrinha'], 'QUEBRA': [], 'lata': ['cobra'], 'latinha': ['latonha', 'loca', 'coca'], 'cobra': [], 'pegasus': [], 'quebrinha': ['quebronha'], 'latonha': [], 'quebronha': [], 'loca': [], 'coca': ['latinhaaaa', 'fanta'], 'latinhaaaa': ['gente'], 'fanta': ['uva', 'junta'], 'uva': ['como'], 'junta': ['luna'], 'luna': [], 'como': [], 'gente': ['ruim'], 'ruim': []}
        self.item_pai = 'raiz'
        self.item_filho = ''
        self.trilha = []
        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        print(f"{Cores.negrito}{Cores.verde}╋{'━━━━'*10}━╋")
        print(f"┃{Cores.limpa}{Cores.verde}{f'Bem Vindo ao Item-Tree':^41}┃")
        print(f"╋━━╋{'━━━━'*8}━━━╋━━╋")

        print(f"{Cores.negrito}{Cores.verde}┃{f'┣❰ {Cores.amarelo}1{Cores.limpa} {Cores.negrito}{Cores.verde}- Executar uma Arvore de Item ❱┫':^60}",
              f"\n{Cores.negrito}{Cores.verde}┃{f'┣━━❰ {Cores.amarelo}2{Cores.limpa} {Cores.verde}- Criar uma Arvore de Item ❱━┫':^56}",
              f"\n┃{f'╋━━━━━━━━━━┳❰ {Cores.amarelo}3{Cores.limpa} {Cores.negrito}{Cores.verde}- Sair ❱┳━━━━━━━━━━━╋':^60}",
              f"\n{Cores.negrito}{Cores.verde}┃{'╋━━━━━━━━━━━━╋':^41}")

        escolha = validar_escolha([1,2,3])

        if escolha == 2:
            self.nome_da_arvore = str(input(f"┗ Nome da Arvore: {Cores.amarelo}"))
            Cores.limpador()
            self.criar_arvore()
        elif escolha ==1:
            print('┣ Em Breve')
        else:
            print('┣ Obrigado por testar!!!')

    def criar_arvore(self):
        os.system("cls")
        len_nome = len(self.nome_da_arvore)+6
        print(f"╋{'━'*len_nome}╋")
        print(f"┃   {Cores.amarelo}{self.nome_da_arvore}{Cores.limpa}   ┃")
        print(f"╋{'━'*len_nome}╋")

        self.criar_lista()

        print(f"╋{'━'*24}╋")
        print(f"┣❰ {Cores.amarelo}1{Cores.limpa} - Salvar Item-Tree ❱┫")
        print(f"┣━❰ {Cores.amarelo}2{Cores.limpa} - Adicionar Item ❱━┫")
        print(f"╋{'━'*24}╋")

        escolha = validar_escolha([1,2])
        if escolha == 1:
            print(f"┣{'━'*15}━")
            self.item_pai = str(input('┃ Item pai: '))
            if self.item_pai == '':
                self.item_pai = 'raiz'
            self.item_filho = str(input('┃ item: '))
            print(f"┗{'━'*15}━")
            sleep(0.5)
            self.adiciona_item(self.item_filho, self.item_pai)
        else:
            print("salvar em breve!!!")
            sleep(1)

        self.criar_arvore()

    def criar_lista(self):
        for item in self.lista_items["raiz"]:
            print(f'*{item}')
            self.verifica_filhos(item)
            self.trilha = []

    def verifica_filhos(self, item):

        for dado in self.lista_items[item]:

            self.trilha.append(not dado == self.lista_items[item][-1])

            print(f'{" "}', end='')
            for espaco in self.trilha[:-1]:
                if espaco:
                    print(f'{"┃"}', end='')
                else:
                    print(f'{" "}', end='')
                print(f'{"  "}', end='')

            if dado == self.lista_items[item][-1]:
                print(f'┗╸{dado}')
            else:
                print(f'┣╸{dado}')

            self.verifica_filhos(dado)

            self.trilha.pop(len(self.trilha)-1)

    def adiciona_item(self, filho, pai='raiz'):
        if pai in self.lista_items:
            self.lista_items[pai].append(filho)
        else:
            self.lista_items[pai] = [filho]

        if filho not in self.lista_items:
            self.lista_items[filho] = []


ItemTree()
