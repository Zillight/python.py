# Fibonacci Sequence 

# Formula: x(n)=x(n-1)+x(n-2)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i))