"""MusicAlbum -> title, artist, year, songs"""

# this allow to refer to the same class we are writing from, in this case method eq, attribute other
from __future__ import annotations
# from typing import List, Dict, Tuple, Optional
# Optional is for optional argument. For example: Optional[List[str] = None] (optional list of strings, default to None)
from typing import List 



class MusicAlbum:

    def __init__(self,
                 title: str,
                 artist: str,
                 year: int,
                 songs: List[str]) -> None:
        self.title = title
        self.artist = artist
        self.year = year
        self.songs = songs

    def __str__(self) -> str:
        return f"MusicAlbum(title='{self.title}', artist='{self.artist}')"

    def __eq__(self, other: MusicAlbum) -> bool:
        if self.title == other.title and self.artist == other.artist:
            return True
        return False


if __name__ == "__main__":
    music_album_1 = MusicAlbum("The Wall",
                             "Pink Floyd",
                             1979,
                             ["ABitW1", "ABitW2"])
    music_album_2 = MusicAlbum("The Dark Side of the Moon",
                               "Pink Floyd",
                               1972,
                               ["Time", "Us and Them"])
    music_album_3 = MusicAlbum("The Wall",
                             "Pink Floyd",
                             1979,
                             ["ABitW1", "ABitW2"])

    print(music_album_1)
    print(music_album_1 == music_album_3)