#exercise 1
def check_int_decorator(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError(f"The argument isn't an int. '{type(args[0])}' passed instead.")
        else:
            return func(*args, **kwargs)
    return wrapper

#exercise 2
def filter_divisible_by(divisor: int):
    def filter_out(func):
        def wrapper(*args, **kwargs):
            results = list(filter(lambda x: x % divisor == 0, func(*args, **kwargs)))
            return results
        return wrapper
    return filter_out

        
@filter_divisible_by(2)
@check_int_decorator
def create_squares_list(stop: int):
   return [n**2 for n in range(stop)]


if __name__ == "__main__":
    l_squared = create_squares_list(10)
    print(l_squared)