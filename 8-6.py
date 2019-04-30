# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters "done". Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

list = []
while True:
    num = input('Enter a number:')
    if num == "done":
        break
    else:
        list.append(int(num))

print("max:", max(list))
print("min:", min(list))
