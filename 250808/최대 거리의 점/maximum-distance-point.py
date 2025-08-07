n,m = map(int, input().split())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

arr.sort()
ans = 0

left = 1
right = 10**9

def check(dist):
    count = 1
    last_index = 0
    for i in range(1,n):
        if arr[i] - arr[last_index] >=dist:
            count+=1
            last_index = i

    return count >= m



while left<=right:
    mid = (left+right) // 2
    if check(mid):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right=mid-1

print(ans)
