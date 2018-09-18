counter = dict()
fileObject = open("words.txt")

for line in fileObject:
    words = line.split()
    for word in words:
        counter[word] = counter.get(word, 0) +1
start = 0
for x, y in counter.items():
    if y > start:
        start = y
        print(x)

