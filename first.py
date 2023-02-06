x = input("First number: ")
y = input("Second number: ")

print(x + y) # When you input x = 10 and y = 20, the answer will be '1020', and that is because it sees everything as strings, like, "10" + "20".
print(type(x))

a = float(input("Third number: "))
b = float(input("Fourth number: "))

print(a + b) # When you input x = 10 and y = 20, the answer will be '30.0' and this is because it has been typecasted into float, (you can equally typecast into int) but float gives the user to input any value. 

print(type(a))