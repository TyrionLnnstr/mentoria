import  requests
import  os 
import  datetime
from dotenv import load_dotenv 
load_dotenv()

class TMDB:
    def head(self):    
        self.Authorization = os.getenv('tmdb_Authorization', None)
        self.header = {"accept": "application/json","Authorization":self.Authorization}

    def url_b(self):   
        self.url_base = 'https://api.themoviedb.org/'

    def endp(self):
        self.endpoint = '/3/discover/movie?'

    def params(self):
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

    def qry(self):
        self.query_params = ''
        self.conct_aux = 0
        for k, v in self.get_params().items():
            if self.conct_aux > 0:
                self.query_params += '&'
        self.query_params += f"{k}={v}"
        self.conct_aux += 1

    def dt_time(self):
        return datetime.datetime.now().strftime("%Y%m%d")

    def get_api(self):
        try:
            self.query()
            self.response = requests.get(self.url_base+self.endpoint+self.query_params, headers=self.header)
            self.response.raise_for_status()
            self.page += 1
        except  requests.exceptions.HTTPError as e:
                print("An HTTP Error occurred: ", e)
        except  requests.exceptions.RequestException as e:
                print("A Request Error occurred: ", e)
        except  Exception as e:
                print("A Exception occurred: ", e)

    def data(self):
        return self.response.json()