# A script that determines if a certain year is a leap year

year = int(input("Enter year: "))

if year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    next_leap_year = year + (4 - year % 4)
    print(f"{year} is not a leap year. The next leap year will be {next_leap_year}.")