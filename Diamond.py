# A python script that requests the user to enter number of rows to display a diamond(palindrome)

rows = int(input("Enter number of rows: "))

# First nested loop to display the upper part of the diamond
for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print("* ", end="") 
    print()      
    
# Second nested loop to display the lower part of the diamond   
for i in range(0, rows - 1):
    for j in range(0, i + 1):
        print(" ", end="") 
    for j in range(0, rows - i - 1):
        print("* ", end="") 
    print()
