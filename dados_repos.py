import requests
import pandas as pd 
from math import ceil

class DadosRepositorios:
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {'Authorization' : 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    def lista_repositorios(self):
        repos_list = []

        response = requests.get(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)

        for page_num in range(1, num_pages):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        return repos_list
    
    def nomes_repos(self, repos_list):
        repos_name = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_name.append(repo['name'])
                except:
                    pass
        return repos_name
    
    def nomes_linguagens(self, repos_list):
        repos_language = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_language.append(repo['language'])
                except:
                    pass
        return repos_language
    
    def dataframe_repositorios(self):

        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios
                                           )
        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados

amazon_repo = DadosRepositorios('amzn')
linguagens_mais_usadas_amazon = amazon_repo.dataframe_repositorios()
# print(linguagens_mais_usadas_amazon)

netflix_repo = DadosRepositorios('netflix')
linguagens_mais_usadas_netflix = netflix_repo.dataframe_repositorios()
# print(linguagens_mais_usadas_netflix)

spotify_repo = DadosRepositorios('spotify')
linguagens_mais_usadas_spotify = spotify_repo.dataframe_repositorios()
# print(linguagens_mais_usadas_spotify)

apple_repo = DadosRepositorios('apple')
linguagens_mais_usadas_apple = apple_repo.dataframe_repositorios()

# Salvando os dados

linguagens_mais_usadas_amazon.to_csv('dados/linguagens_amzn.csv')
linguagens_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
linguagens_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')
linguagens_mais_usadas_apple.to_csv('dados/linguagens_apple.csv')