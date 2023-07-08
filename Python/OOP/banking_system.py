# A simple banking system that utilizes classes

# TODO: Main class that controls the entire script

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
        return f"Account number: {self.account_number}, Account type: {self.account_type}, Balance: {self.balance}"
    
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
    
    def update_info(self, new_name, new_address, new_email):
        self.name = new_name
        self.address = new_address
        self.email = new_email


customers = []

while True:
    command = input("What do you want to do?: ")

    match command:
        case "create customer":
            customer = Customer(input("Enter customer name: "), input("Enter customer address: "), input("Enter customer email: "))
            customers.append(customer)
            print(f"Customer {customer.name} created")
        case "delete customer":
            customer_to_delete = input("Enter customer name to delete: ")
            if len(customers) != 0:
                for customer in customers:
                    if customer.name == customer_to_delete:
                        customers.remove(customer)
                        print(f"Customer {customer_to_delete} deleted")
                    else:
                        print(f"Customer {customer_to_delete} not found")
        case "show customers":
            if len(customers) != 0:
                for customer in customers:
                    print(customer.name)
            else:
                print("No customers")
        case "show customer info":
            customer_to_show = input("Enter customer name to show: ")
            for customer in customers:
                if customer.name == customer_to_show:
                    print(customer.account_info())
                else:
                    print(f"Customer {customer_to_show} not found")
        case "update customer info":
            customer_to_update = input("Enter customer name to update: ")
            for customer in customers:
                if customer.name == customer_to_update:
                    customer.update_info(input("Enter new customer name: "), input("Enter new customer address: "), input("Enter new customer email: "))
                    print(f"Customer {customer_to_update} updated")
                else:
                    print(f"Customer {customer_to_update} not found")
        case "create account":
            account = Account(input("Enter account number: "), input("Enter account type: "), float(input("Balance: ")))
            account_holder = input("Enter account holder name: ")
            for customer in customers:
                if customer.name == account_holder:
                    customer.add_account(account)
                    print(f"Account {account.account_number} created and added to {customer.name}'s accounts")
                else:
                    print(f"Customer {account_holder} not found")
        case "delete account":
            account_to_delete = input("Enter account number to delete: ")
            for customer in customers:
                for account in customer.accounts:
                    if account.account_number == account_to_delete:
                        customer.remove_account(account)
                        print(f"Account {account_to_delete} deleted from {customer.name}'s accounts")
                    else:
                        print(f"Account {account_to_delete} not found")
        case "show accounts":
            customer_to_show = input("Enter customer name: ")
            accounts = "Accounts: \n"
            for customer in customers:
                if customer.name == customer_to_show:
                    for account in customer.accounts:
                        accounts += f"{account.account_number}\n"
            print(accounts)
        case "check account balance":
            account_to_check = input("Enter account number: ")
            for customer in customers:
                for account in customer.accounts:
                    if account.account_number == account_to_check:
                        print(account.check_balance())
                    else:
                        print(f"Account {account_to_check} not found")
        case "show account info":
            account_to_check = input("Enter account number: ")
            for customer in customers:
                for account in customer.accounts:
                    if account.account_number == account_to_check:
                        print(account.account_info())
                    else:
                        print(f"Account {account_to_check} not found")
        case "make a deposit":
            account_to_deposit = input("Enter account number: ")
            amount = int(input("Enter amount to deposit: "))
            for customer in customers:
                for account in customer.accounts:
                    if account.account_number == account_to_deposit:
                        account.deposit(amount)
                        print(f"Deposit of {amount} made to account {account.account_number}. New balance: {account.check_balance()}")
                    else:
                        print(f"Account {account_to_deposit} not found")
        case "make a withdraw":
            account_to_withdraw = input("Enter account number: ")
            amount = int(input("Enter amount to deposit: "))
            for customer in customers:
                for account in customer.accounts:
                    if account.account_number == account_to_withdraw:
                        account.withdraw(amount)
                        print(f"Withdrawl of {amount} made to account {account.account_number}. New balance: {account.check_balance()}")
                    else:
                        print(f"Account {account_to_withdraw} not found")
            pass
        case "dev-test":
            customer = Customer("John Apple", "640 N Mendicant RD", "johna9132@gmail.com")
            account = Account(123, "checking", 69420.0)
            customer.add_account(account)
            customers.append(customer)
        case "exit":
            break
        case _:
            print("Invalid command. Please try again.")
