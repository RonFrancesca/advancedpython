# power dictionary - exercise 1s
power_dictionary = {f"power_{i}": [pow(j, i) for j in range(4)] for i in range(4)}
#print(power_dictionary)

# exercise 2
sample_dict = {
    "a": 1, 
    "b": 4, 
    "c": 17, 
    "d": 16
}  
only_4_dict = {k:v for (k, v) in sample_dict.items() if v % 4 == 0}
print(only_4_dict)