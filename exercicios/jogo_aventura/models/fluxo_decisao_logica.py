from exercicios.jogo_aventura.models.fluxo import Fluxo


class FluxoDecisaoLogica(Fluxo):
    def __init__(self, descricao: str, sim: Fluxo, nao: Fluxo):
        self.sim = sim
        self.nao = nao
        super(FluxoDecisaoLogica, self).__init__(descricao)

