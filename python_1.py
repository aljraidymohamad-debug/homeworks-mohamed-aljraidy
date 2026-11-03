from cs50 import get_int

def printmy(y ,asd ):
    for i in range(y):
        print (asd,end="")

height = get_int("height pyramid : ")

for i in range(height):
    printmy(height-1-i, " ")
    printmy(i+1, "#")
    printmy(1, " ")
    printmy(i+1 ,"#")
    print()
