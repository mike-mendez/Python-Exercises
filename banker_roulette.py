import random

names = input("Give me everybody's name separated by a comma and space\n")
names = names.split(', ')
print(f"{names[random.randint(0, len(names) - 1)]} will be paying tonight.")
