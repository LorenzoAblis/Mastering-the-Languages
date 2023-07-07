# A simple shopping list

shopping_list = []

while True:
    command = input("What do you want to do? (type help for a list of commands): ").lower()

    if command == "help":
        print("Commands: help, add_item, remove_item, show_list, clear_list, exit")
    elif command == "add_item":
        input_item = input("What item do you want to add?: ")
        shopping_list.append(input_item)
        print(f"{input_item} added to your shopping list.")
    elif command == "remove_item":
        input_item = input("What item do you want to remove?: ")
        if input_item in shopping_list:
            shopping_list.remove(input_item)
            print(f"{input_item} removed from your shopping list.")
    elif command == "show_list":
        print(f"Here is your list: {', '.join(shopping_list)}")
    elif command == "clear_list":
        shopping_list.clear()
        print("Your shopping list has been cleared.")
    elif command == "exit":
        break
    else:
        print("Command not found.")
