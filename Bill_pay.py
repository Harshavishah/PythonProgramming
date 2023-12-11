import random

names_string = input("Enter names \n ")
names= names_string.split(", ")


# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(names[random_choice])
print(f"{names[random_choice]} is going to for everybody's food bill today ")
