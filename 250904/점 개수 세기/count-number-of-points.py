from bisect import bisect_left, bisect_right
n,q = map(int, input().split())

points = list(map(int, input().split()))

nums = sorted(set(points))
# for x in points:
#     nums.add(x)
query = [tuple(map(int, input().split())) for _ in range(q)]
U = len(nums)
mapper = {v: i+1 for i, v in enumerate(nums)}

prefix_sum = [0] * (U + 1)
for x in points:
    nx = mapper[x]
    prefix_sum[nx] += 1

for i in range(1, U+1):
    prefix_sum[i] += prefix_sum[i-1]

def get_value(a,b):
    return prefix_sum[b]-prefix_sum[a-1]

for a, b in query:
    new_a = bisect_left(nums, a) + 1
    new_b = bisect_right(nums, b) 
    print(get_value(new_a, new_b))
    
