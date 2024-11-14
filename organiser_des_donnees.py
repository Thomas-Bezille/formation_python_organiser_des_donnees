import re
from pathlib import Path

path = Path("c:/xampp/htdocs/DEV/PYTHON/formation_python_organiser_des_donnees/names.txt")

with open(path, "r", encoding="utf-8") as file:
    content = file.read()
    sanitized_names = re.sub(r"[,\.\n]", " ", content)
    sanitized_names = re.sub(r"\s+", " ", sanitized_names)
    sanitized_names_list = sanitized_names.split(" ")
    