# A simple banking system that utilizes classes


class Account:
    def __init__(self, account_number, account_type, balance):
        self.account_number = str(account_number)
        self.account_type = str(account_type)
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def check_balance(self):
        return self.balance
    
    def account_info(self):
        return f"Account number: {self.account_number}, Account type: {self.account_type}, Balance: ${self.balance}"
    
    def update_info(self, attr, new_attr):
        match attr:
            case "account number":
                self.account_number = new_attr
            case "account type":
                self.account_type = new_attr
            case "balance":
                self.balance = new_attr
            case _:
                print(f"{attr} not found")


class Customer:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)
    
    def remove_account(self, account):
        self.accounts.remove(account)

    def account_info(self):
        account_numbers = ""
        for account in self.accounts:
            account_numbers += f"{account.account_number}\n"

        print(f"Name: {self.name}, Address: {self.address}, Email: {self.email}, Accounts: {account_numbers}")
    
    def update_info(self, attr, new_attr):
        match attr:
            case "name":
                self.name = new_attr
                print(f"Customer name set to {new_attr}")
            case "address":
                self.address = new_attr
                print(f"Customer address set to {new_attr}")
            case "email":
                self.email = new_attr
                print(f"Customer email set to {new_attr}")
            case _:
                print(f"{attr} not found")


class Controller:
    def __init__(self):
        self.customers = []

    def create_customer(self, name, address, email):
        if any(customer.name == name for customer in self.customers):
            print(f"{name} already exists as a customer.")
        else:
            customer = Customer(name, address, email)
            self.customers.append(customer)
            print(f"Customer {customer.name} created")

    def delete_customer(self, name):
        if any(customer.name == name for customer in self.customers):
            for customer in self.customers:
                if customer.name == name:
                    self.customers.remove(customer)
                    print(f"Customer {customer.name} deleted")
        else:
            print(f"Customer {name} does not exist")

    def show_customers(self):
        if len(self.customers) > 0:
            for customer in self.customers:
                print(f"Name: {customer.name}, Address: {customer.address}, Email: {customer.email}")
        else:
            print("No customers")

    def show_customer_info(self, name):
        if any(customer.name == name for customer in self.customers):
            for customer in self.customers:
                if customer.name == name:
                    print(f"Name: {customer.name}\nAddress: {customer.address}\nEmail: {customer.email}")
        else:
            print(f"Customer {name} doesn't exist")

    def update_customer_info(self, name, attr, new_attr):
        if any(customer.name == name for customer in self.customers):
            for customer in self.customers:
                if customer.name == name:
                    customer.update_info(attr, new_attr)
        else:
            print(f"Customer {name} doesn't exist")

    def create_account(self, name, number, type, balance):
        if any(account.account_number == number for customer in self.customers for account in customer.accounts):
            print(f"Account {number} already exists in a customer")
        else:
            account = Account(number, type, balance)
            if any(customer.name == name for customer in self.customers):
               for customer in self.customers:
                    customer.accounts.append(account)
                    print(f"Account {account.account_number} created and added to {customer.name}'s accounts")
            else:
                print(f"Customer {name} not found")

    def delete_account(self, number):
        if any(account.account_number == number for customer in self.customers for account in customer.accounts):
            for customer in self.customers:
                for account in customer.accounts:
                    if account.account_number == number:
                        customer.accounts.remove(account)
                        print(f"Account {number} deleted")
        else:
            print(f"Account {number} not found")

    def show_accounts(self, name):
        if any(customer.name == name for customer in self.customers):
            for customer in self.customers:
                if customer.name == name:
                    for account in customer.accounts:
                        print(account.account_info())
        else:
            print(f"Customer {name} not found")

    def check_balance(self, number):
        if any(account.account_number == number for customer in self.customers for account in customer.accounts):
            for customer in self.customers:
                for account in customer.accounts:
                    if account.account_number == number:
                        print(account.check_balance())
        else:
            print(f"Account {number} not found")

    def show_account_info(self, number):
        if any(account.account_number == number for customer in self.customers for account in customer.accounts):
            for customer in self.customers:
                for account in customer.accounts:
                    if account.account_number == number:
                        print(account.account_info())
        else:
            print(f"Account {number} not found")

    def make_deposit(self, number, amount):
        if any(account.account_number == number for customer in self.customers for account in customer.accounts):
            for customer in self.customers:
                for account in customer.accounts:
                    if account.account_number == number:
                        account.deposit(amount)
                        print(f"Deposited ${amount} to account {number}")
        else:
            print(f"Account {number} not found")

    def make_withdrawl(self, number, amount):
        if any(account.account_number == number for customer in self.customers for account in customer.accounts):
            for customer in self.customers:
                for account in customer.accounts:
                    if account.account_number == number:
                        account.withdraw(amount)
                        print(f"Withdrawn ${amount} to account {number}")
        else:
            print(f"Account {number} not found")
    
    def dev(self):
        self.create_customer("John Apple", "640 N Mendicant RD", "johna9132@gmail.com")
        self.create_account("John Apple", 123, "checking", 69420.0)


class Main:
    def __init__(self):
        self.controller = Controller()
    
    def run(self):
        print("Welcome to the banking system")

        while True:
            command = input("What do you want to do?: ").lower()

            match command:
                case "help":
                    print("\nAvailable commands:\nCreate a customer\nDelete a customer\nShow all customers\nShow customer info\nUpdate customer info\
                          \nCreate an account\nDelete an account\nShow all accounts\nCheck account balance\nShow account info\nMake a deposit\
                          \nMake a withdrawl\nDev\nExit\n")
                case "create a customer":
                    self.controller.create_customer(input("Enter customer name: "), input("Enter customer address: "), input("Enter customer email: "))
                case "delete a customer":
                    self.controller.delete_customer(input("Enter customer name: "))
                case "show all customers":
                    self.controller.show_customers()
                case "show customer info":
                    self.controller.show_customer_info(input("Enter customer name: "))
                case "update customer info":
                    self.controller.update_customer_info(input("Enter customer name: "), input("Select attribute: ").lower(), input("Enter new attribute: "))
                case "create an account":
                    self.controller.create_account(input("Enter customer name: "), input("Enter account number: "), input("Enter account type: "), input("Enter account balance: "))
                case "delete an account":
                    self.controller.delete_account(input("Enter account number: "))
                case "show all accounts":
                    self.controller.show_accounts(input("Enter customer name: "))
                case "check account balance":
                    self.controller.check_balance(input("Enter account number: "))
                case "show account info":
                    self.controller.show_account_info(input("Enter account number: "))
                case "make a deposit":
                    self.controller.make_deposit(input("Enter account number: "), float(input("Enter amount: ")))
                case "make a withdrawl":
                    self.controller.make_withdrawl(input("Enter account number: "), float(input("Enter amount: ")))
                case "dev":
                    self.controller.dev()
                case "exit":
                    break
                case _:
                    print("Invalid command")


main = Main()
main.run()
