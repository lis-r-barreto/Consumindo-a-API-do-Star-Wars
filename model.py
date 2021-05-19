import requests
import json

class Model():
    def __init__(self):
        self.response_personagens = requests.get('https://swapi.dev/api/people/')
        self.personagens = []
        self.response_planetas = requests.get('https://swapi.dev/api/planets/')
        self.planetas = []
        self.response_filmes = requests.get('https://swapi.dev/api/films/')
        self.filmes = []
        self.response_veiculos = requests.get('https://swapi.dev/api/vehicles/')
        self.veiculos = []
        self.response_especies = requests.get('https://swapi.dev/api/species/')
        self.especies = []
        self.response_naves = requests.get('https://swapi.dev/api/starships/')
        self.naves = []

    def gerar_lista_personagens(self):
        # Transformando dados de personagens json em dicionários filtrados por key=results
        dados_personagens = json.loads(self.response_personagens.text)['results']
        # Criando lista de personagens
        for self.personagem in dados_personagens:
            self.personagens.append(self.personagem['name'])
        for self.personagem in self.personagens:
            print(self.personagem)

    def gerar_lista_planetas(self):
        # Transformando dados de planetas json em dicionários filtrados por key=results
        dados_planetas = json.loads(self.response_planetas.text)['results']
        # Criando lista de planetas
        for planeta in dados_planetas:
            self.planetas.append(planeta['name'])
        for self.planeta in self.planetas:
            print(self.planeta)

    def gerar_lista_filmes(self):
        # Transformando dados de filmes json em dicionários filtrados por key=results
        dados_filme = json.loads(self.response_filmes.text)['results']
        # Criando lista de filmes
        for filme in dados_filme:
            self.filmes.append(filme['title'])
        for self.filme in self.filmes:
            print(self.filme)

    def gerar_lista_veiculos(self):
        # Transformando dados de veículos json em dicionários filtrados por key=results
        dados_veiculos = json.loads(self.response_veiculos.text)['results']
        # Criando lista de veículos
        for veiculo in dados_veiculos:
            self.veiculos.append(veiculo['name'])
        for self.veiculo in self.veiculos:
            print(self.veiculo)

    def gerar_lista_naves(self):
        # Transformando dados de naves json em dicionários filtrados por key=results
        dados_naves = json.loads(self.response_naves.text)['results']
        # Criando lista de naves
        for nave in dados_naves:
            self.naves.append(nave['name'])
        for self.nave in self.naves:
            print(self.nave)

    def gerar_lista_especies(self):
        # Transformando dados de espécies json em dicionários filtrados por key=results
        dados_especies = json.loads(self.response_especies.text)['results']
        # Criando lista de espécies
        for especie in dados_especies:
            self.especies.append(especie['name'])
        for self.especie in self.especies:
            print(self.especie)

model = Model()
model.gerar_lista_filmes()