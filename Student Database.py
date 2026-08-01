# Function to print main menu
def menu():
    print("\n\t\t\t=== Student Database ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Show Top Student")
    print("8. Clear Database")
    print("9. Exit")

    print()     # For a line space
    option = input("Enter Your Option : ")

    # Validate Option
    def isValid(option):
        for el in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if(option == el):
                return 1
        return 0

    while not isValid(option):
        print("\nInvalid Option\n")
        option = input("Enter Again : ")

    return option

# Function to add student information
def addInfo(database, id):
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))

    # Validate age
    while age < 1:
        print("\nInvalid Age")
        age = int(input("Enter Again : "))

    depart = input("Enter Department : ")
    cgpa = float(input("Enter cgpa : "))

    # Validate cgpa
    while cgpa < 0 or cgpa > 4:
        print("\nInvalid cgpa")
        cgpa = float(input("Enter Again : "))

    # now add to database
    database[id] = {"Name" : name, "Age" : age, "Depart" : depart, "cgpa" : cgpa}

    return database


# Function to add student ---------
def addStd(database):
    id = input("Enter ID : ")

    # Check if already not exist
    def isExist(id):
        for key in database.keys():
            if(key == id):
                return 1
        return 0

    while isExist(id):
        print("\nID already exist")
        id = input("Enter Again : ")

    # Ask other information 
    database = addInfo(database, id)
    return database

# Funciton to view All students ----------
def viewAll(database):
    print()     # For a line space
    if(len(database) == 0):
        print("\nRecord is Empty\n")
        return
    for key in database.keys():

        print("--------------------------")
        print("Student ID\t: ", key, "\n")
        for k in database[key].keys():
            print(k, "\t: ", database[key][k])
        print()

# Function to search student --------
def searchStd(database):
    print()     # For a line space
    id = input("Enter Student ID : ")
    found = False

    for key in database.keys():
        if(key == id):
            found = True
            print()     # For a line space
            print("--------------------------")
            print("Name\t: ", database[key]["Name"])
            print("Age\t: ", database[key]["Age"])
            print("Depart\t: ", database[key]["Depart"])
            print("cgpa\t: ", database[key]["cgpa"])
            break
    if(not found):
        print("\n\t--- Student Not Found ---")

# Function to update student ----------
def updateStd(database):
    print()     # For a line space
    id = input("Enter Student ID : ")
    found = False

    for key in database.keys():
        if(id == key):
            found = True
            database = addInfo(database, id)
            break

    if(not found):
        print("\n\t--- Student Not Found ---")
    return database

# Function to delete student ---------
def delStd(database):
    print()     # For a line space
    id = input("Enter Student ID : ")
    found = False

    for key in database.keys():
        if(key == id):
            found = True
            del database[key]
            break

    if(not found):
        print("\n\t--- Student Not Found ---")
    return database

# Function to count students ---------
def countStd(database):
    print("\n\tStudents Count : ", len(database))

# Function to show Top Student --------
def showTop(database):
    if(len(database) == 0):
        print("\nDatabase is Empty")
        return
    cgpa = []

    for key in database.keys():
        for k in database[key].keys():
            if(k == "cgpa"):
                cgpa.append(database[key][k])

    maxx = max(cgpa)
    for key in database.keys():
        for k in database[key].keys():
            if(k == "cgpa"):
                if(maxx == database[key][k]):
                    print()     # For a line space
                    print("--------------------------")
                    print("Name\t: ", database[key]["Name"])
                    print("Age\t: ", database[key]["Age"])
                    print("Depart\t: ", database[key]["Depart"])
                    print("cgpa\t: ", database[key]["cgpa"])
    

# Function to clear database --------
def clearAll(database):
    database.clear()
    return database




database = {}            # Initialize empty dictionary

# main loop engine
while True:
    option = menu()

    if(option == '1'):
        database = addStd(database)
    elif(option == '2'):
        viewAll(database)
    elif(option == '3'):
        searchStd(database)
    elif(option == '4'):
        database = updateStd(database)
    elif(option == '5'):
        database = delStd(database)
    elif(option == '6'):
        countStd(database)
    elif(option == '7'):
        showTop(database)
    elif(option == '8'):
        database = clearAll(database)
    else:
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break