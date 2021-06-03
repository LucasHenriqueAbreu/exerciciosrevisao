from exercicios.jogo_aventura.models.fluxo import Fluxo


class FluxoNormal(Fluxo):
    def __init__(self, descricao: str):
        super(FluxoNormal, self).__init__(descricao)
