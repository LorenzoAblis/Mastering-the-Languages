# A calculator that utilizes classes and has history functionality

class Calculator:
    def __init__(self):
        self.history = History()

    def calculate(self, x, y, operation):
        match operation:
            case "+":
                calculation = str(x + y).rstrip('.0')
                self.history.write(calculation)
                return calculation
            case "-":
                calculation = str(x + y).rstrip('.0')
                self.history.write(calculation)
                return calculation
            case "*":
                calculation = str(x + y).rstrip('.0')
                self.history.write(calculation)
                return calculation
            case "/":
                calculation = str(self.divide(x, y)).rstrip('.0')
                self.history.write(calculation)
                return calculation
            case _:
                return "Invalid operation"
            
    def divide(self, x, y):
        if y == 0: 
            return "Cannot divide by zero"
        else:
            return x / y


class History:
    def __init__(self):
        self.history = []
    
    def write(self, calculation):
        if len(self.history) >= 10:
            self.history.pop()
            self.history.append(calculation)
        else:
            self.history.append(calculation)

    def read(self):
        i = 1

        if len(self.history) <= 0:
            print("No history")
        else:
            for calculation in self.history:
                print(f"{i}. {calculation}")
                i += 1
    
    def clear(self):
        self.history = []
        print("History cleared")


class UI:
    def __init__(self):
        self.calculator = Calculator()
    
    def run(self):
        print("----Calculator----")
        print('Type "help" for a list of commands, "q" to exit')

        while True:
            command = input("Enter a command: ")

            match command:
                case "":
                    pass
                case "calculate":
                    print(self.calculator.calculate(float(input("First #: ")), float(input("Second #: ")), input("Operation: ")))
                case "history":
                    self.calculator.history.read()
                case "q":
                    break
                case _:
                    print("Invalid command")


test = UI()
test.run()