from time import perf_counter


def print_time(func):
    def wrapper():
        starting_time = perf_counter()
        func()
        ending_time = perf_counter()
        print(f"the amount of seconds needed to execute the function are: {ending_time - starting_time}")
    return wrapper

@print_time
def create_one_million_squares_list():
    return [n**2 for n in range(1000000)]


if __name__ == "__main__":
    create_one_million_squares_list()
    