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

#6
def move_disk(i):
    x = int(format(i, "b"))
    if x % 2 == 1:
        return 1
    if x % 100000 == 0:
        return 6
    if x % 10000 == 0:
        return 5
    if x % 1000 == 0:
        return 4
    if x % 100 == 0:
        return 3
    if x % 10 == 0:
        return 2

## I know we're supposed to use recursion, but I couldn't figure it out....


#7
## E => N
# def e_to_n(n):
#     if n == 2:
#         return 0
#     elif n % 4 == 0:
#         return 2*n
#     else:
#         return 2*n+1
#
# print(e_to_n(2))
# print(e_to_n(4))
# print(e_to_n(6))

## N => Z
# def n_to_z(n):
#     if n == 1:
#         return 0
#     elif n % 4 == 0:
#         return 2*n
#     else:
#         return 2*n+1
#
# print(n_to_z())
# print(n_to_z(4))
# print(n_to_z(6))
