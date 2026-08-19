# Function to remove duplicate
numbers = []
def remove_dups(numList:list)->list:
    
    newlist = []
    for item in numList:
        if item not in newlist:
            newlist.append(item)
    return newlist




# Function to take numbers
def takeInput():

    nums = int(input("Enter How many Numbers : "))
    print("Enter Duplicate Numbers Below\n")
    i = 0
    while i < nums:
        numbers.append(int(input("Enter : ")))
        i+=1


# Mian Loop
while True:
    print("\t\t\t=== Duplicate Remover ===\n")
    takeInput()
    print("\n Oignal list :\t", numbers)
    numbers = remove_dups(numbers)
    print("\n Processed list :\t", numbers)

    # Option to quit
    option = input("Press q/Q to Exit : ")
    if option == 'q' or option == 'Q':
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break

    print()     # For a line space
    numbers = []        # Clear Old List
    