#Function in Python
def minimum(first, second): #User defined function
    if first > second:
        print(second)
    else:
        print(first)

minimum(1,5) 

print(min(1,5)) # Inbuilt function

# You can use RETURN instead of PRINT in a User defined function

def mini(first, second): #User defined function
    if first > second:
        return(second)
    else:
        return(first)
var = mini(1,5)
print(var)