# A script that calculates the factorial of a number

number = int(input("Enter a number: "))
i, factorial = 1, 1

while i <= number:
    factorial *= i
    i += 1

print("Factorial of", number, "is", factorial)
