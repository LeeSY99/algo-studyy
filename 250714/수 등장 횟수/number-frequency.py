n, m = map(int, input().split())

nums = list(map(int, input().split()))
find_nums = list(map(int, input().split()))

num_dict = dict()

for num in nums:
    if num in num_dict:
        num_dict[num]+=1
    else:
        num_dict[num] = 1

for num in find_nums:
    if num in num_dict:
        print(num_dict[num], end = ' ')
    else:
        print(0, end = ' ')