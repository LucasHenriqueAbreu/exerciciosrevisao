from time import sleep

from exercicios.jogo_aventura.models.fluxo_decisao_logica import FluxoDecisaoLogica
from exercicios.jogo_aventura.models.fluxo_normal import FluxoNormal

def rodar_historia(historias: list):
    for fluxo in historias:
        if isinstance(fluxo, FluxoNormal):
            print(fluxo.descricao)
        elif isinstance(fluxo, FluxoDecisaoLogica):
            print(fluxo.descricao)
            decisao = input('Sim ou não? S/N')
            if decisao in 'Ss':
                print(fluxo.sim.descricao)
            else:
                print(fluxo.nao.descricao)

        print(' ... ')
        sleep(3)


historias = []

historias.append(FluxoNormal('Seja bem vindo a história do joão é o pé de feijão.'))
historias.append(FluxoNormal('Você se chama João e vive com sua mãe em uma humilde casa.\nVocê e sua mãe estão passando por dificuldades e já não tem como se alimentar,\npois o único bem que possuem é uma vaca que já não da mais leite.'))
historias.append(FluxoNormal('Assim, sua mãe lhe pede para levar a vaca até a cidade e vendê-la.'))
historias.append(FluxoDecisaoLogica(
    descricao='Levar a vaca para vendê-la como sua mãe pediu?',
    sim=FluxoNormal('Legal, assim você a caminho da cidade'),
    nao=FluxoNormal('Sua mão te deixou de castigo e você precisou ir de qualquer maneira até a cidade vender a vaca.')
))
historias.append(FluxoNormal('Você sai com a vaca e no meio do caminho, encontra um senhor que lhe oferece feijões mágicos em troca da vaca.'))


rodar_historia(historias)
