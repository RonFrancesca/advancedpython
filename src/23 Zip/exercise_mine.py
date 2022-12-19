# the zip command is really useful if I need to iterate two lists at time
first_names = ["Albert", "Isaac"]
last_names = ["Einstein", "Newton"]

for name, surname in zip(first_names, last_names):
    print(f"Hi! I am {name} {surname}.")