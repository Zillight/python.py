# Scope and Function

num = 20

def multiply(n):
    n = n * 10 # CAn be rewritten as 'n *= 10'
    num = n
    print("The value of num  inside function: ",num)
multiply(num)

print(num) # This is a global variable(outside of the function)