n = int(input())

word_dict = dict()

for _ in range(n):
    word = input()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(max(word_dict.values()))