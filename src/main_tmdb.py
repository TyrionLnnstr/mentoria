import  requests
import  tmdb_api

try:
    response = requests.get(tmdb_api.url+tmdb_api.endp+tmdb_api.query_params, headers=tmdb_api.header)
    response.raise_for_status()

except  requests.exceptions.HTTPError as e:
        print("An HTTP Error occurred: ", e)
except  requests.exceptions.RequestException as e:
        print("A Request Error occurred: ", e)
except  Exception as e:
        print("A Exception occurred: ", e)
data        =   response.json()
pag_total   =   (data['total_pages'])
pag         =   (data['page'])