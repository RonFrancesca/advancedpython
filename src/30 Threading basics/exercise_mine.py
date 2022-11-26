import json
import threading
from pathlib import Path
from typing import Dict, List

NUM_FILE = 8
NUM_THREADS = 4


def _open_json_file(filename: str) -> Dict:
    with open(filename, "r") as file:
        return json.load(file)


def load_json_file(file_list: List[Path], content: List):
    for file in file_list:
        print(f"Filename {file}")
        content.append(_open_json_file(file))
    return content


def generate_file_for_thread(common_root: str, 
                             num_threads: int, 
                             num_files: int) -> List[List[Path]]:
    num_file_for_thread = int(NUM_FILE / NUM_THREADS)
    flatten_files_for_threads = [Path(f"{common_root}{i+1}.json") for i in range(num_files)]
    file_per_thread = [flatten_files_for_threads[i:i+num_file_for_thread] for i in range(0, num_files, num_file_for_thread)]
    return file_per_thread
    


if __name__ == "__main__":

    file_per_thread = generate_file_for_thread('./dummy_', NUM_THREADS, NUM_FILE)

    content = []
    threads = []

    for file in file_per_thread:
        thread = threading.Thread(target=load_json_file, args=(file, content))
        thread.start()
        threads.append(thread)


    for thread in threads:
        thread.join()

    for data in content:
        print(data)

