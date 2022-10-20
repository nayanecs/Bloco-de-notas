from bloco_de_notas import BlocoDeNotas
from nota import Nota


class CriarNotas:
    if __name__ == '__main__':
        # criando três notas
        nota_01 = Nota('19/05/2022 - 12:00', 'Participar ativamente das aulas de programação')
        nota_02 = Nota('19/05/2022 - 12:00', 'Participar ativamente das aulas de matemática')
        nota_03 = Nota('19/05/2022 - 12:00', 'Tirar a melhor nota possível')

        print(nota_01.get_as_json())



        # criando um bloco de notas
        bloco_de_notas = BlocoDeNotas()

        # teste método adicionar_notas
        bloco_de_notas.adicionar_notas(nota_01)
        bloco_de_notas.adicionar_notas(nota_02)
        bloco_de_notas.adicionar_notas(nota_03)

        # teste método imprimir_nota
        bloco_de_notas.imprimir_notas()

        # teste método numero_de_notas
        print(bloco_de_notas.numero_de_notas())

        # teste método exibir_nota
        nota = bloco_de_notas.exibir_nota(2)

        # teste método exibir_nota
        print(nota.descricao_detalhada())

        # teste método remover_nota
        nota_removida = bloco_de_notas.remover_nota(2)
        print(nota_removida.descricao_detalhada())

        bloco_de_notas.imprimir_notas()