myList = []

# print menu
def menu_print():
    print("\t\t\t=== Inventory System ===\n")
    print("1. Add product")
    print("2. View Products")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Calculate Inventory Value")
    print("7. Exit")

    option = input("Enter Your Option : ")

    # Validate Option
    def isValid(option):
        if option in ['1', '2', '3', '4', '5', '6', '7']:
            return True
        else:
            return False

    while not isValid(option):
        print("\nInvalid Option")
        option = input("Enter Again : ")

    return option

# Add product ----------
def addProduct():
    print()     # For a line space
    id = int(input("Enter ID : "))
    name = input("Enter Name : ")
    price = float(input("Enter Price : "))
    quant = int(input("Enter Quantity : "))
    myDict = {}
    myDict["ID"] = id
    myDict["Name"] = name
    myDict["Price"] = price
    myDict["Quantity"] = quant

    myList.append(myDict)

# View Products ----------
def view():
    print()     # For a line space
    for item in myList:
        print(item)

# Search Product ----------
def search():
    print()     # For a line space
    id = int(input("Enter ID of Product : "))
    print()     # For a line space

    for i in range(len(myList)):
        if myList[i]["ID"] == id:
            print("ID : ", id)
            print("Name : ", myList[i]["Name"])
            print("Price : ", myList[i]["Price"])
            print("Quantity : ", myList[i]["Quantity"])
            return
    print("Product Not Found")
        

# Update Product ---------
def update():
    print()     # For a line space
    id = int(input("Enter ID : "))
    print()     # For a line space

    for i in range(len(myList)):
        if myList[i]["ID"] == id:
            name = input("Enter Name : ")
            price = float(input("Enter Price : "))
            quant = int(input("Enter Quantity : "))
            myList[i]["Name"] = name
            myList[i]["Price"] = price
            myList[i]["Quantity"] = quant
            return
    print("Product Not Found")
            

#Function to delete product ------------
def delete():
    print()     # For a line space
    id = int(input("Enter ID : "))
    print()     # For a line space

    for i in range(len(myList)):
        if myList[i]["ID"] == id:
            myList.pop(i)
            return

    print("Product Not Found")

# Calculate Inventry Value ------------
def countValues():
    print()     # For a line space
    id = int(input("Enter ID : "))
    print()     # For a line space

    for i in range(len(myList)):
        if myList[i]["ID"] == id:
            print("Name : ", myList[i]["Name"])
            print("Quantity : ", myList[i]["Quantity"])
            print("Value : ", myList[i]["Price"]*myList[i]["Quantity"])
            return
    print("Product Not Found")

# Main Loop 
while True:
    option = menu_print()

    if option == '1':
        addProduct()
    elif option == '2':
        view()
    elif option == '3':
        search()
    elif option == '4':
        update()
    elif option == '5':
        delete()
    elif option == '6':
        countValues()
    else:
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break

    print()     # For a line space
