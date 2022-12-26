from pathlib import Path
from typing import List, Dict, Optional

from src.project.loading.serialization import Serializer


class LoaderIterator:
    
    def __init__(self, 
                serializer: Serializer,
                num_files_per_iteration: int,
                load_paths: Optional(List[Path])) -> None:
        
        self.serializer: serializer
        self.num_files_per_iteration: num_files_per_iteration
        self._load_paths = load_paths
        self._current_iteraction = None

    @property
    def load_paths(self) -> Optional(List[Path]):
        return self._load_path

    @load_paths.setter
    def load_paths(self, load_paths: List[Path]) -> None:
        self._load_path = load_paths

    def __iter__(self):
        self._current_iteraction = 0
        return self

    def __next__(self) -> List[Dict]:
        if self._did_load_all_batch():
            raise StopIteration
        data_batch = self._load_batch()
        self._current_iteraction += 1
        return data_batch

    def _did_load_all_batch(self):
        if self._current_iteraction >= len(self._load_paths) / self.num_files_per_iteration:
            return True
        return False

    def _load_data_batch(self) -> List[Dict]:
        start_index = self._current_iteraction * self.num_files_per_iteration
        stop_index = start_index + self.num_files_per_iteration
        return [self.serializer.load(load_path) for load_path in self._load_paths[start_index:stop_index] if load_path.exist()]

