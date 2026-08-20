# Global lists
list1 = []
list2 = []

# Function to take input
def takeInput():
    
    print("\t\t\t=== Common Elements in Two Lists ===\n")
    print("Enter List 1 : ")
    len = int(input("Enter Length : "))
    i = 0
    while i < len:
        list1.append(input(" : "))
        i+=1

    print("Enter List 2 : ")
    len = int(input("Enter Length : "))
    i = 0
    while i < len:
        list2.append(input(" : "))
        i+=1

# Function to find common elements
def findCommons():
    list3 = []
    for item in list1:
        if item not in list3:
            if item in list2:
                list3.append(item)



    # set1 = set(list1)
    # set2 = set(list2)

    # set3 = set1.intersection(set2)
    # print(set3)

    return list3

# Main Loop 
while True:
    takeInput()
    processed = findCommons()
    print("\nOrignal Lists :-\n")
    print(list1)
    print(list2)
    print("\nProcessed List :-\n")
    print(processed)

    option = input("Press q/Q to Exit : ")
    if option == 'q' or option == 'Q':
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break
        
    print()     # For a line space