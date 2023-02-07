# Find Function
txt = "Hello, there"
x = txt.find("e")
print(x)
x = txt.find("e", 5, 10) # 5, 10 >> stating the range where it should find e.
print(x)

x = txt.find("x")
print(x) # This will print -1 which means invalid

