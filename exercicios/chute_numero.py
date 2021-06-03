from random import randint


class ChuteNumero:
    def __init__(self):
        self.ranking = []
        self.iniciar()

    def iniciar(self):
        continuar_brincando = True
        while continuar_brincando:
            self.numero_aleatorio = randint(0, 1000)
            self.chute()
            decisao = input('Quer brincar novamente? S/N')
            if decisao in 'Nn':
                continuar_brincando = False

    def chute(self):
        chute_incorreto = True
        quantidade_chutes = 0
        while chute_incorreto:
            try:
                print('De o seu chute, meu caro apedeutinha...')
                chute = int(input('Dica, o número está entre 0 e 1000, fala aí qualé...'))
                if chute == self.numero_aleatorio:
                    self.ranking.append(quantidade_chutes)
                    print(f'Parabéns, apdeuta, você acertou! levou {quantidade_chutes} para acertar')
                    self.mostrar_ranking(quantidade_chutes)
                    chute_incorreto = False
                else:
                    quantidade_chutes += 1
                    if chute > self.numero_aleatorio:
                        print('Tente um número menor')
                    else:
                        print('Tente um número maior')
            except ValueError:
                print('Tente apenas números entre 0 e 1000')

    def mostrar_ranking(self, quantidade_chutes_jogador_atual):
        print(f'Melhor pontuação: {min(self.ranking)}')
        print(f'Pior pontuação: {max(self.ranking)}')
        self.ranking.sort()
        for posicao in self.ranking:
            if posicao == quantidade_chutes_jogador_atual:
                print(f'Você está aqui: {posicao}')
            else:
                print(f'Posição: {posicao}')