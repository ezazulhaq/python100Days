import os
data_file_path = os.path.join(os.path.dirname(__file__), "weather_data.csv")
new_file_path = os.path.join(os.path.dirname(__file__), "new_data.csv")

import pandas

data = pandas.read_csv(data_file_path)
print(data)
print(data["temp"])

temp_list = data["temp"].to_list()
print(temp_list)

# Average temperature
print(data["temp"].mean())

# Max temperature
print(data["temp"].max())

# Min temperature
print(data["temp"].min())


# Get data in column
print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])

# Get row with highest temp
print(data[data.temp == data.temp.max()])

# Get Monday's record
monday = data[data.day == "Monday"]
print(monday.temp)

# Convert Celsius to Fahrenheit
monday_temp_f = (monday.temp * 9/5) + 32
print(monday_temp_f)

# Create a Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_dataframe = pandas.DataFrame(data_dict)
print(data_dataframe)

data_dataframe.to_csv(new_file_path)