# Create a function that will compare two names and display them in order



# list = []
# while True:
#     name = input("Input a name:")
#     if name == "done":
#         break
#     else:
#         list.append(name)
#         list.sort()
#         continue
# print(list)

def sort_names(name1,name2):
    if name1 > name2:
        print(name2)
        print(name1)
    if name2 > name1:
        print(name1)
        print(name2)

print(sort_names("Weekie","Alicia"))

# just want to make sure this goes to GH