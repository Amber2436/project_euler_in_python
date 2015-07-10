with open('/Users/xueyishu/Downloads/names.txt','r') as f:
    words = f.read().split(',')
    words = [list(word.strip('\"')) for word in words]
    f.close()

## sort the list by alphabetical order
words.sort()

def findloc(word):
    loc = 0
    s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in word:
        loc += s.index(i) + 1
    return loc 

totalscore = 0
for i in range(len(words)):
    temp = words[i]
    num = findloc(temp)
    totalscore += (i + 1) * num

print totalscore