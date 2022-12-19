import multiprocessing
from pathlib import Path
from typing import Dict
import json


def save_json_file(data: Dict, path: Path) -> None:
    with open(path, "w") as file:
        return json.dump(data, file)


if __name__ == "__main__":

    data = {"name": "Frodo", "last_name": "Baggins"}

    process1 = multiprocessing.Process(target=save_json_file, args=(data, Path("frodo1.json")), name="process1", daemon=True)
    process2 = multiprocessing.Process(target=save_json_file, args=(data, Path("frodo2.json")), name="process2", daemon=True)

    process1.start()
    process2.start()

    # altrimenti essendo daemon non vengono aspettati
    process1.join()
    process2.join()