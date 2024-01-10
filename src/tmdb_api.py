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

    def get_url(self): 
        return self.url_base
    
    def get_endpoints(self): 
        return self.endpoint

    def get_params(self):
        return {
            'include_adult': self.include_adult,
            'include_video': self.include_video,
            'language': self.language,
            'page': self.page
        }

instancia_base_params = tmdbapi()
url = instancia_base_params.get_url()
endp = instancia_base_params.get_endpoints()
query_params_list = instancia_base_params.get_params()
conct_aux = 0
query_params = ""
for k, v in query_params_list.items():
    if conct_aux > 0:
        query_params += '&'
    query_params += f"{k}={v}"
    conct_aux += 1