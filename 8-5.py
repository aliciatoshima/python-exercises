mbox = open('mbox-short.txt')
count = 0
for line in mbox:
    this_line = line.split()
    print('nemo')
    if this_line[0] == 'From:':
        print(this_line[1])
        count = count + 1
        print('loach')
print(count)
