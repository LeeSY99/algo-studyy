word = list(input())

count = {}

for w in word:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

ans = None
for alpha, c in count.items():
    if c == 1:
        ans = alpha
        break

print(ans)