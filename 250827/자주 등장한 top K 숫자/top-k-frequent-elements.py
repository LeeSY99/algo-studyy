n,k = map(int, input().split())

n_dict = {}

nums = list(map(int, input().split()))
for num in nums:
    if num in n_dict:
        n_dict[num] += 1
    else:
        n_dict[num] = 1

res = []
for num, count in n_dict.items():
    res.append((num,count))

res.sort(key = lambda x: (-x[1],-x[0]))

for i in range(k):
    print(res[i][0], end = ' ')
