import pandas

with open("./data/weather_data.csv") as data_file:
    data_open = data_file.readlines()
    # print(data_open)

data = pandas.read_csv("./data/weather_data.csv")
temp_list = data["temp"].to_list()
print(f"List of Temps Using Pandas: {temp_list}")
print(f"Average Temp: {sum(temp_list) / len(temp_list)}")
print(f"Min Temp: {min(temp_list)} °C")
print(f"Max Temp: {max(temp_list)} °C")
monday = data[data.day == "Monday"]
print(f"Monday's Temp Converted from C to F: {(monday['temp'].item() * 9 / 5) + 32} °F")
