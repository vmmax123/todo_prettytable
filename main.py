import os
import pickle
from prettytable import PrettyTable
from datetime import datetime

# Initialize list for to-do items
todo_list = []
# Filename for storing list items
TODO_FILE = "todo_items.pkl"

# TODO class
class Todo:
    def __init__(self, title, created_time, is_complete=False):
        self.title = title
        self.created_time = created_time
        self.is_complete = is_complete
import os
import pickle
from prettytable import PrettyTable
from datetime import datetime

# Initialize list for to-do items
todo_list = []
# Filename for storing list items
TODO_FILE = "todo_items.pkl"

# TODO class
class Todo:
    def __init__(self, title, created_time, is_complete=False):
        self.title = title
        self.created_time = created_time
        self.is_complete = is_complete

# Write function to save todo_list to file
def save_to_file():
    try:
        # write binaries
        with open(TODO_FILE, "wb") as file:
            pickle.dump(todo_list, file)
    except Exception as e:
        print(f"Error saving file to {e}")

# Read function to load todo_list from file
def read_from_file():
    global todo_list
    if os.path.exists(TODO_FILE):
        try:
            # read binaries
            with open(TODO_FILE, "rb") as file:
                todo_list = pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            print("Error reading from file. File might be corrupted.")
            todo_list = []
        except Exception as e:
            print(f"Error reading from file: {e}")
            todo_list = []

# Print all tasks, generate table using PrettyTable
def print_all_tasks():
    headers = ["ID", "Task", "Date Added", "Complete"]
    x = PrettyTable(headers)
    for i, item in enumerate(todo_list):
        x.add_row([i + 1, item.title, item.created_time, "Yes" if item.is_complete else "No"])
    print(x)

# Create a new item
def add_task():
    title = input('Input task: ')
    created_time = datetime.now().strftime("%d/%m/%y")
    todo_item = Todo(title, created_time)
    todo_list.append(todo_item)
    save_to_file()
    print_all_tasks()

def is_complete():
    print_all_tasks()
    try:
        task_id = int(input("Enter item ID number: ")) - 1
        if 0 <= task_id < len(todo_list):
            todo_list[task_id].is_complete = True
            save_to_file()
            print_all_tasks()
        else:
            print("Oops! Invalid ID")
    except ValueError:
        print("Oops! Invalid input")

# Delete selected item
def delete_task():
    print_all_tasks()
    try:
        task_id = int(input("Enter task ID you wish to delete: ")) - 1
        if 0 <= task_id < len(todo_list):
            del todo_list[task_id]
            save_to_file()
            print_all_tasks()
        else:
            print("Oops! Invalid ID")
    except ValueError:
        print("Oops! Invalid input")

# Reset list
def reset_list():
    global todo_list
    todo_list = []
    save_to_file()
    print("Reset complete. Start new list.")
    print_all_tasks()
    input_options()

def input_options():
    while True:
        user_input = input("Type: 'A' to add an item, 'C' to mark item as completed, 'D' to delete item, 'X' to exit ").upper()
        if user_input == 'A':
            add_task()
        elif user_input == 'C':
            is_complete()
        elif user_input == 'D':
            delete_task()
        elif user_input == 'X':
            print("Goodbye")
            reset_list()
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    os.system('cls' if os.name == "nt" else "clear")
    print("\033[31;1m")  # Set text color to red
    read_from_file()  # Load tasks from file if they exist
    print_all_tasks()  # Display tasks if there are any
    input_options()
