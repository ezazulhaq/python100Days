import os
import csv
data_file_path = os.path.join(os.path.dirname(__file__), "weather_data.csv")

# Read csv file and store in data as list
with open(data_file_path) as data:
    data = data.readlines()
    data = [line.strip().split(",") for line in data]
    print(data)


# Read csv file and store in data as list
with open(data_file_path) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)