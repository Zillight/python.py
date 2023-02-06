# Logical Operators
# OR 
# AND
'''
Rules in OR Operator
True or True = True
True or False = true
False or True = True
False or False = False
'''

'''
Rules for AND Operator
True and True = True
True and False = False
False and False = false
False and False = False
'''

my_bool = True or False
print(my_bool) #True
my_bool = False or False
print(my_bool) #False
my_bool = True and False
print(my_bool) #False
my_bool = False and False
print(my_bool) #False
my_bool = True and True
print(my_bool) #True

print(10 * True)
print(10 * False)