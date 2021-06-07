from exercicios.jogo_aventura.models.fluxo import Fluxo


class FluxoSequecial(Fluxo):
    def __init__(self, descricao: str, fluxos):
        self.fluxos = fluxos
        super(FluxoSequecial, self).__init__(descricao)
