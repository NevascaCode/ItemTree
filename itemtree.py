class ItemTree(object):
    def __init__(self):
        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        print(f"{'-=-='*10}-")
        print(f"{'Bem Vindo ao Item-Tree':^41}")
        print(f"{'-=-='*10}-")

        print("1 - Criar uma Arvore de Item",
              "\n2 - Executar uma Arvore de Item",
              "\n3 - Sair")

ItemTree()
