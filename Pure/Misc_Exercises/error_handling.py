# FileNotFound
# with open("a.file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruits_list = ["Apple", "Banana", "Pear"]
# fruit = fruits_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Error Handling
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     print("File does not exist")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("You fucked up")

# BMI
# height = float(input("Height:\t"))
# weight = int(input("Weight:\t"))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)
#

# INDEX ERROR HANDLING
# fruits = ["Apple", "Pear", "Orange"]
#
#
# # TODO: Catch the exception and make sure the code runs without crashing
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " Pie")
#
#
# make_pie(4)

# KEY ERROR HANDLING
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post["Likes"]
    except KeyError:
        pass

print(total_likes)
