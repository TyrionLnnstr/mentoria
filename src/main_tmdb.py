from tmdb_api import tmdbapi
from file_handler import FileHandler
import datetime
import time

tmdb_instance = tmdbapi()
file_handler = FileHandler()

while True:
    tmdb_instance.get_api()
    dados = tmdb_instance.dados()
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_handler.save_data(dados, current_datetime, tmdb_instance.page)
    if tmdb_instance.page >= dados['total_pages']:
        break

    time.sleep(1)
    tmdb_instance.page += 1