n, q = map(int, input().split())

points = list(map(int, input().split()))

arr = [0] * 1000001
prefix_sum = [0] * 1000001
for point in points:
    arr[point] = 1

prefix_sum[0] = arr[0]
for i in range(1,1000001):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]


for _ in range(q):
    count = 0
    a,b = map(int, input().split())
    if a == 0:
        count += prefix_sum[b]
    else:
        count += prefix_sum[b]-prefix_sum[a-1]
        
    print(count)
    



