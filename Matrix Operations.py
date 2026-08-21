matrix1 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matrix2 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matrix3 = [[0,0,0],         # for transpose
           [0,0,0]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

# Functions to take Input
def takeInput_forAdd():
    print("\nEnter Matrix(3x3) 1 :-")
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            # matrix1.append(int(input(" : ")))
            matrix1[i][j] = int(input(" : "))

    print("\n\n\n", matrix1[0][2])

    print("\nEnter Matrix(3x3) 2 :- ")
    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            # matrix2.append(int(input(" : ")))
            matrix2[i][j] = int(input(" : "))

def takeInput_forTranspose():
    print("Enter Matrix (2x3) :- ")
    for i in range(len(matrix3)):
        for j in range(len(matrix3[0])):
            # matrix3.append(int(input(" : ")))
            matrix3[i][j] = int(input(" : "))


# Function to perform addition
def addMatrix():
    takeInput_forAdd()

    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

# Function to perform transpose of a matrix
def transposeMatrix():
    takeInput_forTranspose()

    rows = len(matrix3)
    cols = len(matrix3[0])

    transpose = []

    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(matrix3[j][i])

        transpose.append(row)

    return transpose
    
# Print Menu
def printMenu():
    print("\t\t\t=== Matrix Operations ===\n")
    print("1. Addition")
    print("2. Transpose")
    print("3. Exit")

    option = input("Enter Your Option : ")

    # Validate Option
    def isValid(option):
        if option in ['1', '2', '3']:
            return True
        else:
            return False

    while not isValid(option):
        print("\nInvalid Option\n")
        option = input("Enter again : ")

    return option

# main loop
while True:
    option = printMenu()

    if option == '1':
        addMatrix()
        print("\nResulted Matrix :- ")
        for row in result:
            print(row)
    elif option == '2':
        transpose = transposeMatrix()
        print("\nOrignal Matrix :-")
        for row in matrix3:
            print(row)
        print("\nTransposed Matrix :-")
        for row in transpose:
            print(row)
    else:
        print("\n\t\t\t=== Thank You! For Using Our Service")
        break
        
    print()     # For a line space

    