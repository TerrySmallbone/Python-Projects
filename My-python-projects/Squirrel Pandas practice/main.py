# with open("weather_data.csv") as weather_data:
#     weather_list = weather_data.readlines()
#     for _ in range(len(weather_list)):
#         weather_list[_ - 1] = weather_list[_ - 1].strip()

# import csv
#
# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     data_list = []
#     for row in data:
#         data_list.append(row)
#     temperatures = []
#     for temp in data_list[1:]:
#         temperatures.append(int(temp[1]))
#     # print(temperatures) # test print

import pandas

# data = pandas.read_csv("weather_data.csv")
## find mean temp
# temp_data = data["temp"].to_list()
# average_temp = sum(temp_data) / len(temp_data)
# print(round(average_temp, 0))
## or
# print(data["temp"].mean())

## find max temp
# print(data["temp"].max())

## find row with max temp
# max_temp = (data.temp.max())
# print(data[data.temp == max_temp])
# ## or
# print(data[data.temp == (data.temp.max())])

## get monday's temp in degrees F
# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32)

## squirrel concensus. fin numbers of each coloured squirrels
## pandas imported above
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

##access Primary Fur Color column
# data.columns = data.columns.str.replace(' ', '_')
# squirrel_colours = data.Primary_Fur_Color
##or by easier way
# squirrel_colours = data["Primary Fur Color"]

##my way below. Works and gives a table but was cheating and skips the lesson
# print(squirrel_colours.unique())
# print(squirrel_colours.value_counts())


### Angela's way
grey_squireel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squireel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squireel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squireel_count)
print(red_squireel_count)
print(black_squireel_count)

data_dict = {
    "Fur Colour": ["Gray", "Red", "Black"],
    "Count": [grey_squireel_count, red_squireel_count, black_squireel_count]
}
data_chart = pandas.DataFrame(data_dict)
print(data_chart)
data_chart.to_csv("squirrel_count")