# A script that can convert between Celcius to Fahrienheit and vice versa

from_unit = input("Convert from: ").lower()
temperature = float(input("Temperature: "))

if from_unit == "C":
    print(f"{temperature}°C = {temperature * 1.8 + 32}°F")
elif from_unit == "F":
    print(f"{temperature}°F = {(temperature - 32) / 1.8}°C")