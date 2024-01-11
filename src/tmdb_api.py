import  requests
import os 
from dotenv import load_dotenv 
load_dotenv()
Authorization = os.getenv('tmdb_Authorization', None)
header = {"accept": "application/json","Authorization":Authorization}

class tmdbapi:
    def __init__(self):
        self.url_base = 'https://api.themoviedb.org/'
        self.endpoint = '/3/discover/movie?'
        self.include_adult = 'false'
        self.include_video = 'false'
        self.language = 'pt-BR'
        self.page = 1
        self.query_params = ''

    def get_params(self):
        return {
            'include_adult': self.include_adult,
            'include_video': self.include_video,
            'language': self.language,
            'page': self.page
        }
    def query(self):
        self.query_params = ''
        self.conct_aux = 0
        for k, v in self.get_params().items():
            if self.conct_aux > 0:
                self.query_params += '&'
        self.query_params += f"{k}={v}"
        self.conct_aux += 1

    def get_api(self):
        try:
            self.query()
            self.response = requests.get(self.url_base+self.endpoint+self.query_params, headers=header)
            self.response.raise_for_status()
            self.page += 1
        except  requests.exceptions.HTTPError as e:
                print("An HTTP Error occurred: ", e)
        except  requests.exceptions.RequestException as e:
                print("A Request Error occurred: ", e)
        except  Exception as e:
                print("A Exception occurred: ", e)
    def dados(self):
        return self.response.json()

tmdb_instance = tmdbapi()
tmdb_instance.get_api()
dados = tmdb_instance.dados()

pag_total   =   (dados['total_pages'])
pag         =   (dados['page'])