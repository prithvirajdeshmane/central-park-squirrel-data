import pandas
from pandas import Series

squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250106.csv")
print(Series.value_counts(squirrel_data['Primary Fur Color']))

gray_squirrels = squirrel_data[squirrel_data['Primary Fur Color'] == "Gray"]
count_gray_squirrels = len(gray_squirrels)
# print (count_gray_squirrels)

cinnamon_squirrels = squirrel_data[squirrel_data['Primary Fur Color'] == "Cinnamon"]
count_cinnamon_squirrels = len(cinnamon_squirrels)
# print (count_cinnamon_squirrels)

black_squirrels = squirrel_data[squirrel_data['Primary Fur Color'] == "Black"]
count_black_squirrels = len(black_squirrels)
# print (count_black_squirrels)

data_dict = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [count_gray_squirrels, count_cinnamon_squirrels, count_black_squirrels]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count_by_color.csv")

print(pandas.read_csv("./squirrel_count_by_color.csv"))