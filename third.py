# Scope and Function 2

num_list = [10, 20, 30, 40, 50]

def multiply(my_list):
    my_list[0] = my_list[0] * 10
    my_list[1] = my_list[1] * 10
    my_list[2] *= 10
    my_list[3] *= 10
    my_list[4] *= 10

multiply(num_list)
print(num_list)