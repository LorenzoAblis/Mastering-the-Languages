# A simple inventory system that utilizes classes


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_attr(self, attr):
        match attr:
            case 'name':
                return self.name
            case 'price':
                return self.price
            case 'quantity':
                return self.quantity
            case _:
                print(f'Attribute {attr} does not exist!')

    def set_attr(self, attr, new_attr):
        match attr:
            case 'name':
                self.name = new_attr
            case 'price':
                self.price = new_attr
            case 'quantity':
                self.quantity = new_attr
            case _:
                print(f'Attribute {attr} does not exist!')


class InventoryTracker:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        if any(product.name == name for product in self.products):
            print(f'Product {name} already exists!')
        else:
            new_product = Product(name, price, quantity)
            self.products.append(new_product)
            print(f'Product {new_product.name} added to inventory')

    def remove_product(self, name):
        if any(product.name == name for product in self.products):
            for product in self.products:
                if product.name == name:
                    self.products.remove(product)
                    print(f'Product {name} removed from inventory')
        else:
            print(f'Product {name} does not exist!')

    def update_product(self, name, attr, new_attr):
        if any(product.name == name for product in self.products):
            for product in self.products:
                if product.name == name:
                    product.set_attr(attr, new_attr)
                    print(f"Updated {attr} of {name} to {new_attr}")
        else:
            print(f'Product {name} does not exist!')

    def show_product(self, name):
        if any(product.name == name for product in self.products):
            for product in self.products:
                if product.name == name:
                    print(f'Name: {product.name}')
                    print(f'Price: ${product.price}')
                    print(f'Quantity: {product.quantity} units')
        else:
            print(f'Product {name} does not exist!')

    def show_all_products(self):
        for product in self.products:
            print(f'Name: {product.name}, Price: ${product.price}, Quantity: {product.quantity} units')


class InventoryController:
    def __init__(self):
        self.it = InventoryTracker()

    def start(self):
        print("Welcome to the Inventory!")

        while True:
            command = input("Type a command (type help for a list of commands): ").lower()

            match command:
                case "help":
                    print("add a product\nremove a product\nshow a product\nshow all products\nupdate a product\nexit")
                case "add a product":
                    self.it.add_product(input("Product name: "), input("Price: "), input("Quantity: "))
                case "remove a product":
                    self.it.remove_product(input("Product name: "))
                case "show a product":
                    self.it.show_product(input("Product name: "))
                case "show all products":
                    self.it.show_all_products()
                case "update a product":
                    self.it.update_product(input("Product name: "), input("Attribute (name, quantity, price): "), input("New value: "))
                case "dev":
                    self.it.add_product('Laptop', 146, 132)
                    self.it.add_product('Mouse', 37, 714)
                    self.it.add_product('Apple', 2, 1243)
                case "exit":
                    break
                case _:
                    print("Invalid command")


main = InventoryController()
main.start()
