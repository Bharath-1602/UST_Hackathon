from collections import Counter

with open('anamoly.log' , 'r') as f:
    for lines in f:
        words = lines.strip()
        print(words)
    