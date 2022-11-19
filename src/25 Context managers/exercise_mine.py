from time import perf_counter

class CodeExecutionTimer:

    def __init__(self) -> None:
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.end_time = perf_counter()
        print(f"The execution time of the code within the with is {self.end_time - self.start_time}")

if __name__ == "__main__":
    with CodeExecutionTimer():
        squares = [n**2 for n in range(100000)]
