class Nota:
    def __init__(self, tempo_agendamento: str, descricao: str):
        self.tempo_agendamento = tempo_agendamento
        self.descricao = descricao

    def descricao_detalhada(self):
        descricao_detalhada = self.tempo_agendamento + '  ' + self.descricao
        return descricao_detalhada

    def get_as_json(self):
        return self.__dict__