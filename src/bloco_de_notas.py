from nota import Nota


class BlocoDeNotas:
    def __init__(self):
        self.proprietario = 'Zé ninguém'
        self.notas = []

    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    def get_proprietario(self):
        return self.proprietario

    def adicionar_notas(self, nota: Nota):
        return self.notas.append(nota)

    def numero_de_notas(self):
        return len(self.notas)

    def imprimir_notas(self):
        for nota in self.notas:
            print(nota.descricao_detalhada())

    def exibir_nota(self, posicao):
        if posicao > len(self.notas):
            print ('Posição inválida')
        else:
            for i in range(len(self.notas)):
                if i == posicao:
                    return self.notas[posicao]

    def remover_nota(self, posicao):
        if posicao > len(self.notas):
            print ('Posição inválida')
        else:
            return self.notas.pop(posicao)

    def get_as_json(self):
        return self.__dict__