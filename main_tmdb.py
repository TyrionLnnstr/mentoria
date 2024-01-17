from src.tmdb_api import TMDB
from src.file_handler import FileHandler
import time

if  __name__ == "__main__":
    
    file_handler  = FileHandler()
    tmdb_instance = TMDB()
    tmdb_instance.get_api()
    data =  tmdb_instance.data()
    
    while True:
        file_handler.save_data(data, tmdb_instance.dt_time(), data['page'])
        if data['page'] >= data['total_pages']:
            break
        time.sleep(1)
        data['page'] += 1