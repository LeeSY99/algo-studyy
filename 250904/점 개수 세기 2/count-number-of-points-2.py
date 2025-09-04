n, q = map(int, input().split())

from sortedcontainers import SortedSet

nums = SortedSet()
prefix_sum = [[0] * (5002) for _ in range(5002)] 

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

for x, y in points:
    nums.add(x)
    nums.add(y)

mapper = {}
cnt = 1
for num in nums:
    mapper[num] = cnt
    cnt += 1

for x,y in points:
    nx, ny = mapper[x], mapper[y]
    prefix_sum[nx][ny] += 1

for i in range(1,cnt + 1):
    for j in range(1, cnt + 1):
        prefix_sum[i][j] += prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

def get_sum(x1,y1,x2,y2):
    return prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]

for _ in range(q):
    x1,y1,x2,y2 = map(int, input().split())
    x1 = nums.bisect_left(x1)+1
    y1 = nums.bisect_left(y1)+1
    x2 = nums.bisect_right(x2)
    y2 = nums.bisect_right(y2)

    ans = get_sum(x1, y1, x2, y2)
    print(ans)
    
