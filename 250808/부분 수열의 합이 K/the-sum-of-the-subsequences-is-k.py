n, k = map(int, input().split())

nums = [0] + list(map(int, input().split()))

prefix_sum = [0] * (n+1)
for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

last = 0

count = 0
for i in range(1,n+1):
    for j in range(i):
        if prefix_sum[i] - prefix_sum[j] == k:
            count +=1

print(count)