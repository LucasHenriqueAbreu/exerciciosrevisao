from exercicios.jogo_aventura.models.fluxo import Fluxo


class FluxoDecisaoMultipla(Fluxo):
    def __init__(self, descricao: str, decisoes: list):
        self.decisoes = decisoes
        super(FluxoDecisaoMultipla, self).__init__(descricao)
