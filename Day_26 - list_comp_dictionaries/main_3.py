weather_c = {
    "Monday": 12,
    "Tuesday": 16,
    "Wednesday": 22,
    "Thursday": 25,
    "Friday": 30,
    "Saturday": 8,
    "Sunday": 33
}

weather_f = {day: (temp_c*9/5)+32 for (day, temp_c) in weather_c.items()}

print(weather_f)