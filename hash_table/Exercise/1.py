arr = []

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        #print(tokens)
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")

#print(arr)

# Average temp in first week of Jan
avg_temp = sum(arr[0:7])/len(arr[0:7])
print(avg_temp)

# Maximum temperature in first 10 days of Jan
max_temp = max(arr[0:10])
print(max_temp)