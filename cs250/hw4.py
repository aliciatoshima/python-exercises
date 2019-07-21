## Homework 4


#1 fibonacci function

def fib(n):
    x = 1
    y = 1

    if n == 1:
        return 1
    if n == 2:
        return 1
        i = i + 1

    if n > 2:
        i = 3
        while i < n+1:
            sum = x + y
            y = x
            x = sum
            i = i + 1
            #print(x)
            #print(y)
    return sum

print(fib(6))




#2 Recursive Fibonnaci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
