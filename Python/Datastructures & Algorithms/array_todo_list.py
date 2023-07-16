# A simple todo list that utilizes arrays

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

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        if any(task.title == title for task in self.tasks):
            return f"Task {title} already exists"
        else:
            self.tasks.append(Task(title, description, due_date))
            return f"Task {title} added"
    
    def remove_task(self, title):
        if any(task.title == title for task in self.tasks):
            for task in self.tasks:
                if task.title == title:
                    self.tasks.remove(task)
                    return f"Task {title} removed"
        else:
            return f"Task {title} not found"
    
    def update_task(self, title, attr, new_attr):
        if any(task.title == title for task in self.tasks):
            for task in self.tasks:
                if task.title == title:
                    task.set_attr(attr, new_attr)
                    return f"Task {title} updated"
        else:
            return f"Task {title} not found"

    def retrive_task(self, title):
        if any(task.title == title for task in self.tasks):
            for task in self.tasks:
                if task.title == title:
                    return task.task_info(one_line=False)
        else:
            return f"Task {title} not found"
        
    def show_tasks(self):
        for task in self.tasks:
            print(task.task_info(one_line=True))

class Interface:
    def __init__(self):
        self.manager = TaskManager()
    
    def run(self):
        print(f"Hello, you have {self.manager.tasks.__len__()} tasks")
        print('Type "help" for a list of commands, "q" to quit')

        while True:
            command = input("What would you like to do?: ").lower()

            match command:
                case "help":
                    print("Add a task\nRemove a task\nShow a task\nShow all tasks \
                          \nUpdate a task\nq")
                case "add a task":
                    print(self.manager.add_task(title=input("Title: "), description=input("Description: "), due_date=input("Date: ")))
                case "remove a task":
                    print(self.manager.remove_task(title=input("Title: ")))
                case "show a task":
                    print(self.manager.retrive_task(title=input("Title: ")))
                case "show all tasks":
                    self.manager.show_tasks()
                case "update a task":
                    print(self.manager.update_task(title=input("Title: "), attr=input("Attribute: "), new_attr=input("New Attribute: ")))
                case "q":
                    break
                case _:
                    print("Invalid command")
        
main = Interface()
main.run()

