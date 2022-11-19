# exercise 1: l = [2, 4 ,16, 80] -> expected_output = [1, 2, 8, 40]
from math import sqrt
from functools import reduce


l = [2, 4 ,16, 80] 
output_l = list(map(lambda x: int(x / 2), l))
print(output_l)

#exercise 2
output_squares = list(filter(lambda x: sqrt(x).is_integer(), l))
print(output_squares)

#l2 = [1, 2, 3] -> expected_output = 6

l2 = [1, 2, 3]
sum_l2 = reduce(lambda a, b: a + b, l2)
print(sum_l2)

# reduce -> return a single value
# map -> return an iterable (map object)
# filter = return an iterable (filter object). The filter does not need a value to add but a value to check.
#          The function (lambda or not) need to return False or True