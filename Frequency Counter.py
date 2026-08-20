# Function to take input
def takeInput():
    print("\t\t\t=== Word/Char Frequency Counter ===\n")
    text = input("Enter : ")
    return text

# Function to count characters
def countCharacters(text:str):
    extraDict = {}

    for char in text:
        if char in extraDict:
            extraDict[char] += 1
        else:
            extraDict[char] = 1

    return extraDict

# Function to count words
def countWords(text:str):
    extraDict = {}
    text = text.split()

    for word in text:
        if word in extraDict:
            extraDict[word] += 1
        else:
            extraDict[word] = 1

    return extraDict

# Funtction to print menu
def printMenu():
    
    print("1. Count Characters")
    print("2. Count Words")
    print("3. Exit")

    option = input("Enter your option : ")

    # Validates Option
    def isValid(option):
        for el in ['1', '2', '3']:
            if option == el:
                return True
        return False

    while not isValid(option):
        print("\nInvalid Option\n")
        option = input("Enter Again : ")
        
    return option

# Main Loop
while True:
    text = takeInput()
    option = printMenu()

    if option == '1':
        print(countCharacters(text))
    elif option == '2':
        print(countWords(text))
    else:
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break
        
    print()     # For a line space
    