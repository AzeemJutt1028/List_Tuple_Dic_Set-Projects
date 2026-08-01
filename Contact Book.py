# Function to print menu
def menu():
    print("\n\t\t\t=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Count Contacts")
    print("7. Clear All")
    print("8. Exit")

    print()     # For a line space
    option = input("Enter Your Option : ")

    # Validate Option
    def isValid(option):
        for el in ['1', '2', '3', '4', '5', '6', '7', '8']:
            if(option == el):
                return 1
        return 0

    while not isValid(option):
        print("\nInvalid Option\n")
        option = input("Enter Again : ")

    return option

# Function to initialize contact book
def initializeBook():
    book = {
        "Azeem" : '0326 4071054',
        "Ali" : '0307 9435141'
    }
    return book

# Function to add contact
def addContact(book):
    print()     # For a line space
    key = input("Enter Name : ")
    value = input("Enter Phone (03xx xxxxxxx) : ")

    book[key] = value

    return book

# Function to View Contacts
def viewContact(book):
    print()     # For a line space

    for key, val in book.items():
        print(key," : ", val);

# Function to Search contct
def searchContact(book):
    print()     # For a line space
    key = input("Enter Name to search : ")
    print("Contact : ", book.get(key))

# Function to Update contact
def updateContact(book):
    print()     # For a line space
    key = input("Enter Name to Updated : ")
    phone = input("Enter Updated Phone (03xx xxxxxxx) : ")

    book[key] = phone
    return book

# Function to delete contact
def delContact(book):
    print()     # For a line space
    key = input("Enter Name to Delete : ")

    del book[key]
    return book

# Function to count contacts
def count(book):
    print("Contacts Count : ",len(book))

# Function to clear all
def clearAll(book):
    book.clear()
    return book

# main system loop 
book = initializeBook()
while True:
    option = menu()

    if(option == '1'):
        book = addContact(book)
    elif(option == '2'):
        viewContact(book)
    elif(option == '3'):
        searchContact(book)
    elif(option == '4'):
        book = updateContact(book)
    elif(option == '5'):
        book = delContact(book)
    elif(option == '6'):
        count(book)
    elif(option == '7'):
        book = clearAll(book)
    else:
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break