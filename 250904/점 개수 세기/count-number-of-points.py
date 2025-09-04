from sortedcontainers import SortedSet
n,q = map(int, input().split())

points = list(map(int, input().split()))

nums = SortedSet()
for x in points:
    nums.add(x)

mapper = {}
cnt = 1
for num in nums:
    mapper[num] = cnt
    cnt += 1

prefix_sum = [0] * cnt
for x in points:
    nx = mapper[x]
    prefix_sum[nx] += 1

for i in range(1,cnt):
    prefix_sum[i] += prefix_sum[i-1]

def get_value(a,b):
    return prefix_sum[b]-prefix_sum[a-1]

for _ in range(q):
    a,b = map(int, input().split())
    new_a = nums.bisect_left(a) + 1
    new_b = nums.bisect_right(b) 
    print(get_value(new_a, new_b))
    
