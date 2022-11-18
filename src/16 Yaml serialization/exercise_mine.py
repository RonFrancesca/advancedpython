from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

import joblib

from musicalbum import MusicAlbum


class Serializer(ABC):

    @abstractmethod
    def dump(self, obj: Any, save_path: Path) -> None:
        pass

    @abstractmethod
    def load(self, load_path: Path) -> Any:
        pass


class JoblibSerializer(Serializer):

    def __init__(self, 
                compress: int = 3) -> None:
        
        self.compress = compress
        
    def dump(self, obj: Any, save_path: Path) -> None:
        with open(save_path, "wb") as file:
            joblib.dump(obj, file, compress=self.compress)

    def load(self, load_path: Path) -> Any:
        with open(load_path, "rb") as file:
            return joblib.load(file)


if __name__ == "__main__":
    params = {
        "title": "The Wall",
        "artist": "Pink Floyd",
        "year": 1979,
        "songs": ["ABitW1", "ABiTW2"]
    }
    the_wall = MusicAlbum(**params)
    path = Path("the_wall.joblib")

    joblib_serializer = JoblibSerializer()
    joblib_serializer.dump(the_wall, path)
    the_wall_2 = joblib_serializer.load(path)
    print(the_wall_2)

