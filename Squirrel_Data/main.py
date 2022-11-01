import pandas

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(f"Average Temp: {sum(temp_list) / len(temp_list)}")
# print(f"Min Temp: {min(temp_list)}")
# print(f"Max Temp: {max(temp_list)}")
# monday = data[data.day == "Monday"]
# print(monday.astype({'temp': 'int'}))
# c_to_f = (monday.temp * 9 / 5) + 32
# print(f"Monday's Temp Converted from C to F:\t{(monday.temp.to_string(index=False) * 9 / 5) + 32}")
# print(data[data.temp == data.temp.max()])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("Squirrel_Count.csv")
