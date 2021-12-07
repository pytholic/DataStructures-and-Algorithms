

weather_dict = {}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature.Ignore the row")


print(weather_dict)

# What was the temperature on Jan 9
print(weather_dict['Jan 9'])

# What was the temperature on Jan 4
print(weather_dict['Jan 4'])