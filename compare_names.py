# Create a function that will compare two names and display them in order



list = []
while True:
    name = input("Input a name:")
    if name == "done":
        break
    else:
        list.append(name)
        list.sort()
        continue
print(list)
