word = list(input())
n = len(word)
count = {}

ans = 0
j = 0
for i in range(n):
    while j<n and word[j] not in count:
        count[word[j]] = 1
        j+=1
    
    ans = max(ans, j-i)
    count.pop(word[i])

print(ans)