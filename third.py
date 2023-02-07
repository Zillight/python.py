# Map(), list() and Filter () - Functions 

# syntax: map(function, list)

num_list = [1, 2, 3, 4, 5]
var = map(lambda n: n*2, num_list)
print(list(var)) 

# Result: [2, 4, 6, 8, 10]