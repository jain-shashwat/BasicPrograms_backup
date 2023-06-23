# with open("weather_data.csv") as data_files:
#     data = data_files.readlines()\
#     print(data)
#
# import csv
# with open("weather_data.csv") as info:
#     data = csv.reader(info)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data["temp"])

# data_dict =data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# avg = sum(temp_list) / len(temp_list)
# print(avg)

# print(data["temp"].mean())
#
# print(data["temp"].max())
# print(data.temp.max())

# print(data["condition"])
# print(data.condition)

## GET ROW IN TABLE
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

## create a dataframe
# data_dict = {
#     "alfa" : ["a", "b", "c"],
#     "position": [1,2,3]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("alfa_csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = {
    "Fur Color" : ["grey", "red", "black"],
    "Count": [0, 0, 0]
}


for count in data["Primary Fur Color"]:
    if count == "Gray":
        data_dict["Count"][0] += 1
    elif count == "Cinnamon":
        data_dict["Count"][1] += 1
    elif count == "Black":
        data_dict["Count"][2] += 1

print(data_dict)

tocsv = pandas.DataFrame(data_dict)
tocsv.to_csv("s_count")









