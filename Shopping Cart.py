# Function to Print Mene and Take Option
def menu():
    print("\t\t\t=== Shopping Cart Calculator ===")
    print()     # For a line space
    print("1. Add Item")
    print("2. View Cart")
    print("3. Calculate Item Total")
    print("4. Calculate Grand Total")
    print("5. Exit")

    option = input("Enter Your Option : ")

    # Validates option
    def isValid(option):
        for el in ['1','2','3','4','5']:
            if(el == option):
                return True
        return False

    while not isValid(option):
        print("\nInvalid Option\n")
        option = input("Enter Again : ")

    return option

# Function to Initialize cart list
def initialize():
    cart = []
    print("Initialized")
    return cart

# Function to add item
def addItem(cart):
    print()     # For a line space
    name = input("Enter Name : ")
    item = int(input("Enter Quantity : "))
    price = float(input("Enter Price : "))
    dictt = {
        "Name" : name,
        "Price" : price,
        "Quantity" : item
    }
    cart.append(dictt)

    return cart

# Function to view cart
def view(cart):
    print()     # For a line space
    
    for i in range(len(cart)):
        print()     # For a line space
        print("Item : ",i)
        print("------------------------")
        for key,val in cart[i].items():
            print(key,":",val)


# Function to calculate item total
def itemTotal(cart):
    print()     # For a line space
    total = 0
    for i in range(len(cart)):
        total += cart[i]["Quantity"]

    print("Item Total : ", total)

# Function to calculate Grand total
def grandTotal(cart):
    print()     # For a line space
    total = 0
    for i in range(len(cart)):
        total += cart[i]["Price"]*cart[i]["Quantity"]

    print("Grand Total : ", total)

cart = initialize()     # Initializes an empty list of items

# Main Loop
while True:
    option = menu()

    if(option == '1'):
        cart = addItem(cart)
    elif(option == '2'):
        view(cart)
    elif(option == '3'):
        itemTotal(cart)
    elif(option == '4'):
        grandTotal(cart)
    else:
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break

    print()     # For a line space
