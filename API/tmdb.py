import requests
import json
import os 
from dotenv import load_dotenv 


'''
Requests  - consultar APIS
OS - consultar dados do Sistema Operacional ** DOTENV e o nosso arquivo especial para guardar os segredos.
Json - manipulacao de arquivos .json
'''


load_dotenv() 
Authorization = os.getenv("tmdb_Authorization")


'''
Neste caso em questão foi importado o objeto Authorization com segredo para conexao a API
'''


include_adult = "false"
include_video = "false"
language = "pt-BR"
page = "1"

parametros = f"include_adult={include_adult}&include_video{include_video}&language={language}&page{page}"

url = f"https://api.themoviedb.org/3/discover/movie?{parametros}"
headers = {"accept": "application/json","Authorization":Authorization}
response = requests.get(url, headers=headers)


'''
neste trecho nos colocamos no codigo qual a url no qual vamos fazer o get
por ser uma API privada necessitamos informar o segredo dentro do cabecalho
por seguranca foi utilizado o arquivo .env para acessar o segredo
'''

if response.status_code == 200:
    data = response.json()
    file = open("mentoria(eng.dados)/data/tmdb.json", "w", encoding=("utf-8")) 
    json.dump(data, file, ensure_ascii=False, indent=2)
else:
    print(response.content)

'''
response.json acessa o get e o transforma em json
---------------------------------------------------
open foi utilizado para criar nosso arquivo como 
nome "tmdb.json"
modo de escrita "w" - caso existam dados eles serão sobrescrito
codificacao "utf-8"
---------------------------------------------------
dump utilizamos o ensure_ascii = false 
isso faz com que os caracteres especiais como acentos sejam exibidos no arquivo
caso contrario teremos resultados como este fam\u00edlia  onde \u00ed representa i com acento
'''