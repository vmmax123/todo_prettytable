import os
import pickle
from prettytable import PrettyTable
from datetime import datetime

# pickle plays role of database

# Init list for to-do items
todo_list = []
# filename for storing list items
TODO_FILE = "todo_items.pkl"

# TODO class
class Todo():
    def __init__(self, title, created_time, is_complete=False):
        self.title = title
        self.created_time = created_time
        self.is_complete = is_complete

# write function
def save_to_file():
    with open(TODO_FILE, "wb") as file:
        pickle.dump(todo_list, file)

# read function, save as pickle
def read_from_file():
    global todo_list
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "rb") as file:
            todo_list = pickle.load(file)
    else:
        todo_list = []  # Initialize to an empty list if the file does not exist


# check first list
def first_time():
    if os.path.exists(TODO_FILE):
        read_from_file()
        print_all_tasks()
    else:
        print("Welcome! Let's get started!")
        add_task()
        print_all_tasks()

# print all items in list

def print_all_tasks():
    headers = ["id", "task", "date added", "complete"]
    x = PrettyTable(headers)
    for i, item in enumerate(todo_list):
        x.add_row([i +1, item.title, item.created_time, "Yes" if item.is_complete else "No"])
    print(x)

# create a new item
def add_task():
    title = input('input task: ')
    created_time = datetime.now().strftime("%d/%m/%y  %H:%M")
    todo_item = Todo(title, created_time)
    todo_list.append(todo_item)
    # Save to pickle file
    save_to_file()
    print_all_tasks()


def is_complete():
    print_all_tasks()
    try:
        task_id = int(input("enter item ID number: ")) -1
        if 0 <= task_id <len(todo_list):
            todo_list[task_id].is_complete = True
            save_to_file()
            print_all_tasks()
        else:
            print("Oops! Invalid ID")
    except ValueError:
        print("Oops! Invalid input")


# Deletes selected item
def delete_task():
    print_all_tasks()
    try:
        task_id = int(input("Enter task ID you wish to delete: ")) - 1
        if 0 <= task_id < len(todo_list):
            del todo_list[task_id]
            # save and reload
            save_to_file()
            print_all_tasks()
        else:
            print("Oops! Invalid ID")
    except ValueError:
        print("Oops! Invalid input")




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
            break
        else:
            print("Invalid input. Try again.")

        print_all_tasks()

if __name__=="__main__":
    #clears console
    os.system('cls' if os.name == "nt" else "clear")
    # color of print (red)
    print("\033[31;1m")
    first_time()
    read_from_file()
    print_all_tasks()
    input_options()
