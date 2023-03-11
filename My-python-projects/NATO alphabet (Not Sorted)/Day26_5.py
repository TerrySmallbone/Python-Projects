weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# 🚨 Don't change code above 👆
# Write your code 👇 below:

## function just used for shits and giggles ##


def c_to_f(temp_c):
    temp_f = temp_c * 9/5 + 32
    return temp_f

weather_f = {day:c_to_f(temp_c) for (day, temp_c) in weather_c.items()}

print(weather_f)