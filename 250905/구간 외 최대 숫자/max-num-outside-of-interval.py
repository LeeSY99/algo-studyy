n,q = map(int, input().split())

nums = list(map(int, input().split()))

L = [0] * n
R = [0] * n

for i in range(n):
    if i == 0:
        L[i] = nums[i]
    else:
        L[i] = max(L[i-1], nums[i])

for i in range(n-1,-1,-1):
    if i == n-1:
        R[i] = nums[i]
    else:
        R[i] = max(R[i+1], nums[i])

for _ in range(q):
    a,b = map(int, input().split())
    print(max(L[a-2], R[b]))