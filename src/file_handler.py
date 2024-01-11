import  json
import  datetime
import  tmdb_api
from    pathlib     import Path

current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

class FileHandler:
    def save_data(self, data, current_datetime, page):
        self.file_name = f"tmdb_{current_datetime}_page{tmdb_api.pag}.json" 
        self.caminho = Path("mentoria(eng.dados)") / "data" / self.file_name
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(tmdb_api.dados, file, ensure_ascii=False, indent=2)