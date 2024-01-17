import json
from pathlib import Path

class FileHandler:
    def save_data(self, data, date, page):
        self.file_name = f"tmdb_{date}_page{page}.json" 
        self.caminho = Path('extract_tmdb','data','{self.file_name}')
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
