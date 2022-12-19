import multiprocessing
import json
from pathlib import Path
from typing import Dict

def save_json(dict_to_save: Dict, filename: Path) -> None:
    with open(filename, "w") as file:
        return json.dump(dict_to_save, file)
 

if __name__ == "__main__":

    frodo = {"name": "Frodo", "last_name": "Baggins"}
    data = [(frodo, Path("frodo_1.json")), (frodo, Path("frodo_2.json"))]
    processes = multiprocessing.Pool(2)
    processes.starmap(save_json, data)
    processes.close()