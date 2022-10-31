import random
import string

user_pwd = ""
print("Welcome to the PyPassword Generator!\n")
input_letters = int(input("How many letters would you like in your password?\t"))
input_numbers = int(input("How many numbers would you like in your password?\t"))
input_symbols = int(input("How many symbols would you like in your password?\t"))

for i in range(input_letters - round(input_letters/2)):
    user_pwd += string.ascii_lowercase[random.randrange(26)]
for j in range(round(input_letters/2)):
    user_pwd += string.ascii_uppercase[random.randrange(26)]
for k in range(input_numbers):
    user_pwd += string.digits[random.randrange(10)]
for m in range(input_symbols):
    user_pwd += string.punctuation[random.randrange(32)]

user_pwd = list(user_pwd)
random.shuffle(user_pwd)
print(f"\nPassword Generated: {''.join(user_pwd)}")


