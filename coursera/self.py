def maxx(array):
    compare = 0
    for i in array:
        if i > compare:
            compare = i
    return compare

def smoll(array):
    compare = 100
    for i in array:
        if i < compare:
            compare = i
    return compare

print(maxx([4,5,3,78,9,0]))
print(smoll([4,5,3,78,9,0,90]))
