n = int(input())
from sortedcontainers import SortedDict

sd = SortedDict()

for _ in range(n):
    word = input()

    if word in sd:
        sd[word] +=1
    else:
        sd[word] = 1

for word, count in sd.items():
    print(word, count)