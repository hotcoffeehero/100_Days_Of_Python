import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")
# # print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average )

# print(data[data.day == 'Monday'])

data = pandas.read_csv('squirrel_data.csv')
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    'Fur Color': ["Gray", "Cinnamon", "Black"],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')