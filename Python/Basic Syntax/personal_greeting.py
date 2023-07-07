# A script that generates a greeting based on their name and age and prints out a personalized message

name = input("What is your name?: ")
age = int(input("What is your age?: "))
personal_message = ""

if age < 18:
    personal_message = "Enjoy life while you can!"
elif age >= 18 and age < 65:
    personal_message = "Save enough money for retirement!"
elif age >= 65:
    personal_message = "Time is limited, do whatever you want before its too late!"

print(f"Hello, {name}! You are {age} years old! {personal_message}")
