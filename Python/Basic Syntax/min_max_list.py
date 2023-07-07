# A script that finds the min or max integer in a list

numbers = input("Enter numbers seperated by a comma: ")
min_or_max = input("Enter 'min' or 'max': ")
numbers_list = numbers.split(",")

if min_or_max == "min":
    print(min(numbers_list))
else:
    print(max(numbers_list))


