# Dictonary of word count in a sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
print({word: len(word) for word in sentence.split()})


# Convert weather_c dictonary to weather_f dictonary
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
}

weather_f = {day: (c * 9/5) + 32 for (day, c) in weather_c.items()}
print(weather_f)