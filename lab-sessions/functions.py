# Part 1

def bmr_calculation(weight, height, age):
    bmr_male = (13.7516*weight) + (5.0033*height) - (6.755*age) + 66.473
    bmr_female = (9.5634*weight) + (1.8496*height) - (4.6756*age) + 655.0955

    chocolate_bar_calories = 214
    male_chocolate = round(bmr_male/chocolate_bar_calories)
    female_chocolate = round(bmr_female/chocolate_bar_calories)

    print(f"male BMR: {bmr_male}", f"female BMR: {bmr_female}", f"male number of chocolate bars: {male_chocolate}", f"female number of chocolate bars: {female_chocolate}")

weight = float(input("weight in kg: "))
height = float(input("height in cm: "))
age = int(input("age in years: "))

bmr_calculation(weight, height, age)


# Part 2

temperature = float(input("temperature in celsius: "))

def celsius_to_fehrenheit(temperature):
    fehrenheit = temperature * (9/5) +32
    print(f"temperature in fehrenheit: {fehrenheit}")

celsius_to_fehrenheit(temperature)


# Part 3

number_seconds = float(input("number of seconds: "))

def seconds_calculation(number_seconds):
    hours = int(number_seconds/3600)
    minutes = int((number_seconds % 3600) / 60)
    seconds = int(number_seconds % 60)
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")

seconds_calculation(number_seconds)
    
    
    






