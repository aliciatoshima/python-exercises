# Create a function that finds the largest number in an array or list. Use arguments and returned values in your solution.

my_list = [2,5,-8,0,89,53]

def my_max(list):
    # that would be too easy
    # return max(list)
    maxx = None
    for i in list:
        if maxx == None:
            maxx = i
        if maxx < i:
            maxx = i
    return maxx



print(my_max(my_list))
