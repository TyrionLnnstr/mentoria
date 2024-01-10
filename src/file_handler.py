import  json
import  datetime
import  main_tmdb
from    pathlib     import Path

current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = Path("mentoria(eng.dados)") / "data" / f"tmdb_{current_datetime}_page{main_tmdb.pag}.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(main_tmdb.data, file, ensure_ascii=False, indent=2)