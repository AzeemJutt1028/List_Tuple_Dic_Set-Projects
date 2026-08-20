# Global List to take numbers
numbers = []

# Fucntion to take input
def takeInput():
    
    nums = int(input("Enter How Many Numbers : "))
    i = 0
    while i < nums:
        numbers.append(int(input("Enter : ")))
        i+=1

# Function to sort assecending order
def sortForward():
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp


# Function to sort reverse
def sortReverse():
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] < numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

# Function to print menu
def menu():
    print("\t\t\t=== List Sorting ===\n")
    print("1. Sort Forward")
    print("2. Sort Reverse")  
    print("3. Exit")  

    option = input("Enter Your Option : ")

    # Validates Option
    def isValidate(option):
        for item in ['1', '2', '3']:
            if(option == item):
                return True
        return False

    while not isValidate(option):
        print("\nInvalid Option\n")
        option = input("Enter Again : ")

    return option

# Main Loop
while True:
    option = menu()

    if option == '1':
        takeInput()
        sortForward()
        print("Sorted List :\t", numbers)
    elif option == '2':
        takeInput()
        sortReverse()
        print("Sorted List :\t", numbers)
    else:
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break
        
        print()     # For a line space
        numbers = []
