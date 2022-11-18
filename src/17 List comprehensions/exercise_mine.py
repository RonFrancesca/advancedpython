from math import sqrt

#square root fo numbers from 0 to 10
square = [sqrt(i) for i in range(10)]
print(square)
print("\n")

#square and square root
final_list = [sqrt(i) if i % 3 == 0 else i**2 for i in range(20)]
print(final_list)
print("\n")

#matrix generation [ [0, 0, 0], [0, 1, 2], [0, 2, 4], [0, 3, 6] ]
matrix = [[i*j for i in range(3)] for j in range(4)]
print(matrix)
print("\n")
        
