# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come grom each email address, and print the dictionary.

# basically exercise 8-5 to start
mbox = open('mbox-short.txt')
list = []
dict = dict()
for line in mbox:
    this_line = line.split()
    if len(this_line) <1:
        continue
    if this_line[0] == 'From:':
        list.append(this_line[1])
for email in list:
    dict[email] = dict.get(email,0) +1
print(dict)
