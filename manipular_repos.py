import requests
import base64

class ManipularRepositorios:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {'Authorization' : 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    def cria_repo(self, nome_repo):
        data = {
            'name': nome_repo,
            'description': 'Repositorio com as linguagens utilizadas em determinada empresa.',
            'private': False
        }

        response = requests.post(f'{self.api_base_url}/user/repos', json=data, headers=self.headers)
        print(f'status_code da criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, path):
        # Codificando o arquivo
        with open(path, 'rb') as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)
        # Fazendo o upload
        url = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'
        data = {
                'message': 'Adicionando um novo arquivo no formato .csv',
                'content': encoded_content.decode('utf-8')
            }
        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code da criação do arquivo: {response.status_code}')

# Instanciando o objeto
novo_repo = ManipularRepositorios('ChangCarlos')

# Criando o repositório 
nome_repo = 'linguagens-repositorios'
novo_repo.cria_repo(nome_repo)

# Adicionando arquivos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_apple.csv', 'dados/linguagens_apple.csv')