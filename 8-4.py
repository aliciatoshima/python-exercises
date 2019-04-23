romeo = open('romeo.txt')
list = []
for line in romeo:
    this_line = line.split()
    for word in this_line:
        #print(word)
        if word not in list:
            list.append(word)
list.sort()
#print(list)

answer = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

print(answer == list)
