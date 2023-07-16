# A simple todo list using linked lists


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def set_attr(self, attr, new_attr):
        match attr:
            case "title":
                self.title = new_attr
            case "description":
                self.description = new_attr
            case "due date":
                self.due_date = new_attr
            case _:
                print("Invalid Attribute")
    
    def task_info(self, one_line):
        if one_line:
            return f"Title: {self.title} Description: {self.description} Due Date: {self.due_date}"
        else:
            return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}"


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class TaskManager:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add_task(self, task):
        current = self.head
        while current != None:
            if task.title == current.task.title:
                return f"Task {task.title} already exists!"
            current = current.next

        if current == None:
            new_node = Node(task)

            if self.is_empty():
                self.head = new_node
            else:
                current = self.head
                while current.next != None:
                    current = current.next
                current.next = new_node
            return f"Task {task.title} added"

    def delete_task(self, task_title):
        if self.is_empty():
            return "No tasks"
        
        if self.head.task.title == task_title:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        while current != None:
            if current.task.title == task_title:
                return f"Task {task_title} deleted"
            prev = current
            current = current.next
        
        if current == None:
            return f"Task {task_title} not found"
        
        prev.next = current.next

    def update_task(self, task_title, attr, new_attr):
        if self.is_empty():
            return "No tasks"
        
        current = self.head
        while current != None:
            if current.task.title == task_title:
                current.task.set_attr(attr, new_attr)
                return f"{task_title}'s {attr} set to {new_attr}"
            current = current.next
             
        if current == None:
            return "Task not found"
            
    def display_task(self, task_title):
        if self.is_empty():
            return "No tasks"

        current = self.head
        while current != None:
            if current.task.title == task_title:
                return f"{current.task.task_info(False)}"
            current = current.next

        if current == None:
            return "Task not found"
    
    def display_all_tasks(self):
        if self.is_empty():
            return "No tasks"

        current = self.head
        while current != None:
            print(f"{current.task.task_info(True)}")
            current = current.next


class Interface:
    def __init__(self):
        self.manager = TaskManager()

    def run(self):
        print('Type "help" for a list of commands, "q" to quit')

        while True:
            command = input("What would you like to do?: ").lower()

            match command:
                case "help":
                    print("Add a task\nRemove a task\nShow a task\nShow all tasks \
                          \nUpdate a task\nq")
                case "add a task":
                    print(self.manager.add_task(Task(input("Title: "), input("Description: "), input("Due Date: "))))
                case "remove a task":
                    print(self.manager.delete_task(input("Title: ")))
                case "show a task":
                    print(self.manager.display_task(input("Title: ")))
                case "show all tasks":
                    print(self.manager.display_all_tasks())
                case "update a task":
                    print(self.manager.update_task(input("Title: "), input("Attribute: "), input("New Attribute: ")))
                case "q":
                    break
                case "dev":
                    self.manager.add_task(Task("Task 1", "Description 1", "213"))
                    self.manager.add_task(Task("Task 2", "Description 2", "23r23"))
                    self.manager.add_task(Task("Task 3", "Description 3", "wefe"))
                case _:
                    print("Invalid command")


main = Interface()
main.run()

