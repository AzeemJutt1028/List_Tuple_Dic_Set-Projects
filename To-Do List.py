print("\t\t\t=== To-Do List ===")

# Function to print main menu
def menu():
    print()
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Clear All Tasks")
    print("6. Exit")

    print()     # For a line space
    option = input("Enter Your Option : ")

    # Validate Option
    def isValid(option):
        for el in ['1', '2', '3', '4', '5', '6']:
            if(option == el):
                return 1
        return 0

    while not isValid(option):
        print("\nInvalid Option\n")
        option = input("Enter Again : ")

    return option

# Funciton to initialize list with some work
def initialize():
    list = ['Learning Python', 'Learning Linux', 'Pyhton Scripting']
    return list

# Function to view task
def viewTask(task):
    print()     # For a line space
    for i, el in enumerate(task, start=1):
        print(i, el)

# Fucntion to Add Task
def addTask(task):
    print()     # For a line space
    t = input("Enter Task : ")
    task.append(t)

    return task

# Function to remove task
def remove(task):
    print()     # For a line space
    for i, el in enumerate(task, start=1):
        print(i, el)

    print()     # For a line space
    op = int(input("Enter Number of Task : "))

    while op < 1 or op > len(task):
        print("\nInvalid Option\n")
        op = int(input("Enter Task Number Again : "))

    task.pop(op-1)
    return task

# Function tomark task as completed
def markTask(task):
    print()     # For a line space
    for i, el in enumerate(task, start=1):
        print(i, el)

    print()     # For a line space
    op = int(input("Enter Number of Task : "))
    while op < 1 or op > len(task):
        print("\nInvalid Option\n")
        op = int(input("Enter Task Number Again : "))

    task[op-1] = "✔ "+task[op-1]
    return task

# Function to clear all tasks
def clearAll(task):
    task.clear()
    return task

# main system loop
task = initialize()
while True:
    option = menu()

    if(option == '1'):
        viewTask(task)
    elif(option == '2'):
        task = addTask(task)
    elif(option == '3'):
        task = remove(task)
    elif(option == '4'):
        task = markTask(task)
    elif(option == '5'):
        task = clearAll(task)
    else:
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break

    print()     # For a line space