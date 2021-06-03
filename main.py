from time import sleep

from exercicios.simulador_dado_rpg import SimuladorDadoRpg
from exercicios.chute_numero import ChuteNumero


def obtem_opcao_programa():
    print('Qual programa deseja executar?')
    opcao_incorreta = True
    while opcao_incorreta:
        print('SIMULADOR DE DADO PARA RPG (opção 1)')
        print('CHUTE O NÚMERO (opção 2)')
        print('JOGO DE AVENTURA (opção 3)')
        try:
            decisao = int(input('Informe sua decisão?'))
            if decisao not in (1, 2, 3):
                raise ValueError()
        except ValueError:
            print('Opção invalida')
        else:
            opcao_incorreta = False

    return decisao


def main():
    decisao = obtem_opcao_programa()
    if decisao == 1:
        print('Executando SIMULADOR DE DADO PARA RPG...')
        sleep(1)
        SimuladorDadoRpg()
    elif decisao == 2:
        print('Executando CHUTE O NÚMERO...')
        sleep(1)
        ChuteNumero()
    else:
        print('Executando JOGO DE AVENTURA...')
        sleep(1)


if __name__ == '__main__':
    main()


