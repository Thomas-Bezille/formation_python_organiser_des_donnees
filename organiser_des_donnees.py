import re
from pathlib import Path

ORIGIN_PATH = Path("c:/xampp/htdocs/DEV/PYTHON/formation_python_organiser_des_donnees")
ORIGIN_FILE = ORIGIN_PATH / "names.txt"
DESTINATION_FILE = ORIGIN_PATH / "sorted_names.txt"

with open(ORIGIN_FILE, "r", encoding="utf-8") as file:
    content = file.read()
    sanitized_names = re.sub(r"[,\.\n]", " ", content)
    sanitized_names = re.sub(r"\s+", " ", sanitized_names)
    sanitized_names_list = sanitized_names.split(" ")
    
with open(DESTINATION_FILE, "w", encoding="utf-8") as file:
    sanitized_names_list.sort()
    for name in sanitized_names_list:
        if name == "":
            continue
        file.write(name + "\n")