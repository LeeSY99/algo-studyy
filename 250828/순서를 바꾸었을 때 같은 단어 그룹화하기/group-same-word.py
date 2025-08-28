n = int(input())

word_dict = {}


for _ in range(n):
    word = list(input())
    word.sort()

    word2 = ''
    for w in word:
        word2 += w

    if word2 in word_dict:
        word_dict[word2] += 1
    else:
        word_dict[word2] = 1

 
ans = 0
for g, c in word_dict.items():
    ans = max(ans,c)

print(ans)

    