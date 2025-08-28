n = int(input())

word_dict = {}


for _ in range(n):
    word = input()
    a = {}
    for w in word:
        if w in a:
            a[w] += 1
        else:
            a[w] = 1
    
    word_type = []
    for alpha, count in a.items():
        word_type.append((alpha,count))
    word_type.sort(key = lambda x: (x[0]))
    word2 = ''
    for i, c in (word_type):
        for j in range(c):
            word2 += i
    if word2 in word_dict:
        word_dict[word2] +=1
    else:
        word_dict[word2] = 1

 
ans = 0
for g, c in word_dict.items():
    ans = max(ans,c)

print(ans)

    