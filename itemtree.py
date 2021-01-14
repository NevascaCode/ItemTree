'''ItemTree'''

from Cores import Cores
from time import sleep
import json
import os

def validar_escolha(lista_escolha=[]):
    '''Valida Escolha'''
    while True:
        try:
            Cores.limpador()
            escolha = int(input(f"{Cores.verde}┣ Escolha: {Cores.amarelo}"))
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
        self.lista_items = {"raiz": [{"cor":f"{Cores.verde}"}]}
        self.trilha = []
        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        print(f"{Cores.negrito}{Cores.verde}╋{'━━━━'*10}━╋")
        print(f"┃{Cores.limpa}{Cores.verde}{f'Bem Vindo ao Item-Tree':^41}┃")
        print(f"╋━━╋{'━━━━'*8}━━━╋━━╋")

        print(f"{Cores.negrito}{Cores.verde}┃{f'┣❰ {Cores.amarelo}1{Cores.limpa} {Cores.negrito}{Cores.verde}- Executar uma Arvore de Item ❱┫':^60}",
              f"\n{Cores.negrito}{Cores.verde}┃{f'┣━━❰ {Cores.amarelo}2{Cores.limpa} {Cores.verde}- Criar uma Arvore de Item ❱━┫':^56}",
              f"\n┃{f'╋━━━━━━━━━━╋❰ {Cores.amarelo}3{Cores.limpa} {Cores.negrito}{Cores.verde}- Sair ❱╋━━━━━━━━━━━╋':^60}",
              f"\n{Cores.negrito}{Cores.verde}┃{'╋━━━━━━━━━━━━╋':^41}")

        escolha = validar_escolha([1,2,3])

        if escolha == 1:
            arquivo = str(input(f"{Cores.negrito}{Cores.verde}┗ Nome do arquivo: {Cores.amarelo}"))
            with open(arquivo, "r") as arquivo:
                dados_arquivo = json.load(arquivo)
                self.lista_items = dados_arquivo["arvore"]
                self.nome_da_arvore = dados_arquivo["nome"]
            self.criar_arvore()
        elif escolha == 2:
            self.nome_da_arvore = str(input(f"{Cores.negrito}{Cores.verde}┗ Nome da Arvore: {Cores.amarelo}"))
            Cores.limpador()
            self.criar_arvore()
        else:
            print(f'{Cores.negrito}{Cores.verde}┣ Obrigado por testar!!!')
        Cores.limpador()

    def criar_arvore(self):
        os.system("cls")
        len_nome = len(self.nome_da_arvore)+6
        print(f"╋{'━'*len_nome}╋")
        print(f"┃   {Cores.amarelo}{self.nome_da_arvore}{Cores.limpa}   ┃")
        print(f"╋{'━'*len_nome}╋")

        self.desenhar_arvore()

        print(f"╋{'━'*24}╋")
        print(f"┣❰ {Cores.amarelo}1{Cores.limpa} - Salvar Item-Tree ❱┫")
        print(f"┣━❰ {Cores.amarelo}2{Cores.limpa} - Adicionar Item ❱━┫")
        print(f"╋{'━'*24}╋")

        escolha = validar_escolha([1,2])
        if escolha == 1:
            self.salvar_arvore()
        elif escolha == 2:
            self.adiciona_galho()
        else:
            print("Informe uma opção porra")

        self.criar_arvore()

    def desenhar_arvore(self):
        for item in self.lista_items["raiz"][1:]:
            print(f'*{item}')
            self.desenhar_item_galhos(item)
            self.trilha = []

    def desenhar_item_galhos(self, item):

        for dado in self.lista_items[item][1:]:
            self.trilha.append({"galho":dado != self.lista_items[item][-1], "corl":self.lista_items[dado][0]["cor"]})

            for espaco in self.trilha[:-1]:
                if espaco["galho"]:
                    print(f'{espaco["corl"]}{"┃"}', end='')
                else:
                    print(f'{" "}', end='')
                print(f'{"  "}', end='')

            if dado == self.lista_items[item][-1]:
                print(f'{self.lista_items[dado][0]["cor"]}┗╸{dado}')
            else:
                print(f'{self.lista_items[dado][0]["cor"]}┣╸{dado}')

            self.desenhar_item_galhos(dado)

            self.trilha.pop(len(self.trilha)-1)

    def adiciona_galho(self):
        print(f"┣{'━'*15}━")
        while True:
            try:
                item_pai = str(input('┃ Item pai: '))
                if item_pai == '':
                    item_pai = 'raiz'
                if item_pai in self.lista_items or item_pai == 'raiz':
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"{Cores.vermelho}┣ Não existe esse item{Cores.limpa}")

        item_filho = str(input('┃ item: '))

        cor = self.escolher_cor()

        print(f"┗{'━'*15}━")
        sleep(0.5)

        if item_pai in self.lista_items:
            self.lista_items[item_pai].append(item_filho)
        else:
            self.lista_items[item_pai] = [item_filho]

        if item_filho not in self.lista_items:
            self.lista_items[item_filho] = [{"cor": cor}]

    def escolher_cor(self):
        print(f"{Cores.verde}╋{'━'*50}╋")
        print(f"{Cores.verde}┃{Cores.preto}┣ 1 = Preto", end="")
        print(f"{Cores.negrito}{Cores.preto}{'┣ 9 = Negrito Preto':>29}{Cores.limpa}{Cores.verde}{'┃':>11}")
        Cores.limpador()

        print(f"{Cores.verde}┃{Cores.vermelho}┣ 2 = Vermelho", end="")
        print(f"{Cores.negrito}{Cores.vermelho}{'┣ 10 = Negrito Vermelho':>30}{Cores.limpa}{Cores.verde}{'┃':>7}")
        Cores.limpador()
        print(f"{Cores.verde}┃{Cores.verde}┣ 3 = Verde", end="")
        print(f"{Cores.negrito}{Cores.verde}{'┣ 11 = Negrito Verde':>30}{Cores.limpa}{Cores.verde}{'┃':>10}")
        Cores.limpador()
        print(f"{Cores.verde}┃{Cores.amarelo}┣ 4 = Amarelo", end="")
        print(f"{Cores.negrito}{Cores.amarelo}{'┣ 12 = Negrito Amarelo':>30}{Cores.limpa}{Cores.verde}{'┃':>8}")
        Cores.limpador()
        print(f"{Cores.verde}┃{Cores.azul}┣ 5 = Azul", end="")
        print(f"{Cores.negrito}{Cores.azul}{'┣ 13 = Negrito Azul':>30}{Cores.limpa}{Cores.verde}{'┃':>11}")
        Cores.limpador()
        print(f"{Cores.verde}┃{Cores.rosa}┣ 6 = Rosa", end="")
        print(f"{Cores.negrito}{Cores.rosa}{'┣ 14 = Negrito Rosa':>30}{Cores.limpa}{Cores.verde}{'┃':>11}")
        Cores.limpador()
        print(f"{Cores.verde}┃{Cores.ciano}┣ 7 = Ciano", end="")
        print(f"{Cores.negrito}{Cores.ciano}{'┣ 15 = Negrito Ciano':>30}{Cores.limpa}{Cores.verde}{'┃':>10}")
        Cores.limpador()
        print(f"{Cores.verde}┃{Cores.branco}┗╸ 8 = Branco", end="")
        print(f"{Cores.negrito}{Cores.branco}{'┗╸ 16 = Negrito Branco':>30}{Cores.limpa}{Cores.verde}{'┃':>8}")
        Cores.limpador()
        print(f"{Cores.verde}╋{'━'*50}╋")
        escolha = validar_escolha([1, 2, 3])
        if escolha == 1:
            return f"{Cores.preto}"
        elif escolha == 2:
            return f"{Cores.vermelho}"
        elif escolha == 3:
            return f"{Cores.verde}"
        elif escolha == 4:
            return f"{Cores.amarelo}"
        elif escolha == 5:
            return f"{Cores.azul}"
        elif escolha == 6:
            return f"{Cores.rosa}"
        elif escolha == 7:
            return f"{Cores.ciano}"
        elif escolha == 8:
            return f"{Cores.branco}"
        elif escolha == 9:
            return f"{Cores.negrito}{Cores.preto}"
        elif escolha == 10:
            return f"{Cores.negrito}{Cores.vermelho}"
        elif escolha == 11:
            return f"{Cores.negrito}{Cores.verde}"
        elif escolha == 12:
            return f"{Cores.negrito}{Cores.amarelo}"
        elif escolha == 13:
            return f"{Cores.negrito}{Cores.azul}"
        elif escolha == 14:
            return f"{Cores.negrito}{Cores.rosa}"
        elif escolha == 15:
            return f"{Cores.negrito}{Cores.ciano}"
        elif escolha == 16:
            return f"{Cores.negrito}{Cores.branco}"
        else:
            print("Okay sem cor")
    def salvar_arvore(self):
        with open(self.nome_da_arvore + ".json", "w") as arquivo:
            dados = {"nome":self.nome_da_arvore, "arvore": self.lista_items}
            json.dump(dados, arquivo, indent=3)
        print(f"{Cores.negrito}{Cores.verde}┗ Salvo com Sucesso!{Cores.limpa}")
        sleep(0.5)


ItemTree()
