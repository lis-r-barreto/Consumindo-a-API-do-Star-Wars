from view import View
from model import Model

class Controller():

    def start(self):
        view = View()
        opcao = view.start()
        self.consulta(opcao)

    def consulta(self, opcao):
        view_terminal = View()
        resposta = Model()

        if opcao == 1:
           view_terminal.mostrar_filmes()
           resposta.gerar_lista_filmes()

        elif opcao == 2:
           view_terminal.mostrar_personagens()
           resposta.gerar_lista_personagens()

        elif opcao == 3:
           view_terminal.mostrar_planetas()
           resposta.gerar_lista_planetas()

        elif opcao == 4:
           view_terminal.mostrar_especies()
           resposta.gerar_lista_especies()

        elif opcao == 5:
           view_terminal.mostrar_naves()
           resposta.gerar_lista_naves()

        elif opcao == 6:
           view_terminal.mostrar_veiculos()
           resposta.gerar_lista_veiculos()

        else:
           view_terminal.finalizar()