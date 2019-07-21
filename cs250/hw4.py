## Homework 4

#1 Fibonacci Function

def fib(n):
    list = []
    sum = 0
    i = 0

    if i == 0:
        sum = 0
        i = i+1
        return sum

    if i == 1:
        sum = 1
        i = i+1
        return sum

    while i < n+1:
        sum = fib(i-1) + fib(i-2)
        i = i +1
    return sum
    return i

    print(sum)
    return "A"


fib(3)
