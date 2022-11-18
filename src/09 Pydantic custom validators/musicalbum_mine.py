"""MusicAlbum -> title, artist, year, songs"""

from typing import List

# third classe after the python classes
from pydantic import BaseModel, validator


CURRENT_YEAR = 2022

class MusicAlbum(BaseModel):
    title: str
    artist: str
    year: int
    songs: List[str]
    years_from_publication: str = None

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.years_from_publication = CURRENT_YEAR - self.year

    @validator("year")
    @classmethod
    def check_year_is_in_range(cls, value: int) -> int:
        # def check_year_is_in_range(cls, value: int, values: dic (in case I'd need the other values too for any reason)) -> int:
        supported_year_range = {"min": 1920, "max": 2022}
        if not supported_year_range["min"] <= value <= supported_year_range["max"]:
            message = f"'{value}' value isn't in supported year range: {supported_year_range}"
            raise ValueError(message)
        else:
            return value


if __name__ == "__main__":
    params = {
        "title": "The Wall",
        "artist": "Pink Floyd",
        "year": 1979,
        "songs": ["ABitW1", "ABitW2"]
    }

    music_album_1 = MusicAlbum(title="The Wall",
                               artist="Pink Floyd",
                               year=1979,
                               songs=["ABitW1", "ABitW2"])
    
    music_album_2 = MusicAlbum(**params)
    print(music_album_2.years_from_publication)
