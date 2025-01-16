# # import csv
# # from idlelib.configdialog import is_int
# #
# # with open("./weather_data.csv", mode="r") as data_file:
# #     data = csv.reader(data_file)
# #     #print(data)
# #
# #     temperatures = []
# #     for row in data:
# #         print(row)
# #         if is_int(row[1]):
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
# from copyreg import clear_extension_cache
#
# import pandas
# from pandas import Series
#
# data = pandas.read_csv("./weather_data.csv")
# print(data)
# # print(data["temp"])
#
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)
#
# # print(Series.mean(data["temp"]))
# # print(Series.max(data["temp"]))
#
# # print(data[data.temp == Series.max(data["temp"])])
#
# def celsius_to_fahrenheit(celsius):
#     """Converts Celsius to Fahrenheit."""
#     return (celsius * 9/5) + 32
#
# monday = data[data.day == "Monday"]
# print(f"\n\n{monday}\n")
#
# monday_f = celsius_to_fahrenheit(monday.temp[0])
# print(f"{monday_f} deg F")

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