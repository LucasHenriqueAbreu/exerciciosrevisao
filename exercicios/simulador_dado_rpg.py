from random import randint
from time import sleep

from utils.limpa_console import clean


class SimuladorDadoRpg:
    def __init__(self):
        print('Programa Simulador de dado para RPG está rodando.')
        self.iniciar()

    def iniciar(self):
        continuar_no_programa = True
        while continuar_no_programa:
            self.dado = self.pedir_opcao_dado()
            continuar_rodando_dado = True
            while continuar_rodando_dado:
                self.rolar_dado()
                decisao = input('Deseja rolar o dado novamente? S/N')
                if decisao in 'Nn':
                    continuar_rodando_dado = False

            decisao_programa = input('Deseja escolher outro dado? S/N')
            if decisao_programa in 'Nn':
                print('Finalizando programa...')
                sleep(1)
                clean()
                continuar_no_programa = False


    def pedir_opcao_dado(self):
        print('Informe qual dado você quer usar: ')
        print('D4 - opção 4\nD6 - opção 6\nD8 - opção 8\nD10 - opção 10\nD12 - opção 12\nD20 - opção 20')
        opcao_incorreta = True
        while opcao_incorreta:
            try:
                decisao = int(input('Informe sua decisão'))
                if decisao not in (4, 6, 8, 10, 12, 20):
                    raise ValueError()
            except ValueError:
                print('Opção inválida')
            else:
                opcao_incorreta = False
        return decisao

    def rolar_dado(self):
        print('Rolando dados...')
        sleep(0.8)
        print(f'Dado caiu com o lado: {randint(1, self.dado)}')
