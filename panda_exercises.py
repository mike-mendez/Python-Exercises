import pandas
import random
import re

file1 = [1, 2, 3]
file2 = [2, 3, 4]

# new_list = [new_item for item in list if test]
overlap = [int(num) for num in file1 if num in file2]
# print(overlap)

# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {name: random.randint(1, 100) for name in names}
# print(student_scores)
passed_students = {key: value for (key, value) in student_scores.items() if value >= 60}
# print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# print(re.split("[\b\W\b]", sentence))

word_length = {word: len(word) for word in re.split("[\b\W\b]", sentence) if len(word) > 0}
# print(word_length)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
student_scores_data = {
    "student": list(student_scores.keys()),
    "score": list(student_scores.values())
}

student_scores_df = pandas.DataFrame(student_scores_data)
for index,row in student_scores_df.iterrows():
    print(row.score)
