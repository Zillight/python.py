# Map(), list() and Filter () - Functions 

# syntax: map(function, list)
# syntax: filter(function, list)

num_list = [1, 2, 3, 4, 5]
var = map(lambda n: n*2, num_list)
print(list(var)) # This list serves as a form of typecasting 

# Result: [2, 4, 6, 8, 10]

var = filter(lambda n: n>2, num_list)
print(list(var)) 

# Result: [3, 4, 5]
