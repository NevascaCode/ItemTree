class Cores(object):
    negrito = '\033[1m'

    preto = '\033[30m'
    vermelho = '\033[31m'
    verde = '\033[32m'
    amarelo = '\033[33m'
    azul = '\033[34m'
    rosa = '\033[35m'
    ciano = '\033[36m'
    branco = '\033[37m'

    limpa = '\033[0m'
    def limpador():
        print('\033[0m', end='')
