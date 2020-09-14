# Using a loop, sum all of the whole numbers stored in an array or list (assume there are “length” numbers stored in the array)

array = [1,2,3,4,5]

def my_sum(array):
    cur_sum = 0
    for i in array:
        cur_sum = i + cur_sum
    return cur_sum

print(my_sum(array))

array2 = [5,1,2,3,4,5]

def my_sum_2(array):
    curr_sum = 0
    for i in array[1:]:
        curr_sum = i + curr_sum
    return curr_sum

print(my_sum_2(array2))

#test