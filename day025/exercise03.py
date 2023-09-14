import os
import pandas
data_file_path = os.path.join(os.path.dirname(__file__), "Squirrel_Data.csv")
squirrel_count_file_path = os.path.join(os.path.dirname(__file__), "squirrel_count.csv")

data = pandas.read_csv(data_file_path)
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv(squirrel_count_file_path)