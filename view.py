from art import *
from time import sleep

class View():
    def start(self):
        tprint('Star Wars')
        return self.menu()

    def menu(self):
        print(
            '-------- MENU --------\n'
              '[1] Filmes\n'
              '[2] Personagens\n'
              '[3] Planetas\n'
              '[4] Espécies\n'
              '[5] Naves\n'
              '[6] Veículos\n'
              '[0] Sair\n'
              )
        return int(input("\nEscolha uma das rotas: "))

    def mostrar_personagens(self):
        print("Personagens Star Wars")

    def mostrar_planetas(self):
        print("Planetas Star Wars")

    def mostrar_filmes(self):
        print("Filmes Star Wars")

    def mostrar_veiculos(self):
        print("Veículos Star Wars")

    def mostrar_especies(self):
        print("Espécies Star Wars")

    def mostrar_naves(self):
        print("Naves Star Wars")

    def finalizar(self):
        print('Encerrando o programa...')
        sleep(2)
        print('Programa encerrado!')
        exit()
