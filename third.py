# Recursion

def count(num):
    print(num)
    #Base case
    if num == 0:
        return 0
        
    count(num -1)

count(10)
