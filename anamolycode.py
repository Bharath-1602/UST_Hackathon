from collections import Counter

with open('anamoly.log' , 'r') as f:
    lines = f.read()
words = lines.split()
lineslist = lines.split('\n')

wordCount = Counter(words)
tot = sum(wordCount.values())
rarewords = []
for i in wordCount.keys():
    t = wordCount[i]
    if (t/tot)*100 < 1:
        rarewords.append(i)

count = 1
for i in lineslist:
    for j in rarewords:
        if j in i:
            print(count)
    count += 1
    