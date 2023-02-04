print(10 & 20) # 01010 & 10100 base 2 = 0
print(10 | 20) # 01010 | 10100 = 11110 base 2,converting to base 10 = 30
print(10 ^ 20) # 01010 XOR 10100 = 11110 base 2.
print(10>>2) # 1010 right shift 2 will give 10 base 2 = 2 base 10
print(20>>2) #10100 shift 2 = 101, to base 10 = 5
print(5<<1) # 101 left shift 2 = 1010 = 10 base 10
print(10<<2) # 1010 left shift 2 = 101000 = 40 base 10

'''
Addition in Binary
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10
'''
'''
Right Shifting a -ve value
(10 >> 1)
step 1: convert to base 2 = 1010
step 2: add zeros in front to make it 8 bits = 0000 1010
step 3: Do the opposite of all the numbers = 1111 0101
step 4: Add 1 to it ie 11110101 + 1 = 11110110
step 5: shift one place to the right
step 6: add negative to the first number and covert to base 10.
'''
print(-10 >> 1)
print(-20 >> 3)

