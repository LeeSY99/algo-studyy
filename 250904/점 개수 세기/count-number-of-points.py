from sortedcontainers import SortedSet
n,q = map(int, input().split())

points = list(map(int, input().split()))

nums = SortedSet(points)
# for x in points:
#     nums.add(x)
query = [tuple(map(int, input().split())) for _ in range(q)]
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

for a, b in query:
    new_a = nums.bisect_left(a) + 1
    new_b = nums.bisect_right(b) 
    print(get_value(new_a, new_b))
    
