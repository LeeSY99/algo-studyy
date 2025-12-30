n = int(input())
arr = list(map(int, input().split()))

l = 0
r = len(arr)-1

ans = float('inf')
a1,a2 = l, r
while l<r:
    s = arr[l] + arr[r]
    if abs(s) < ans:
        ans = abs(s)
        a1 = arr[l]
        a2 = arr[r]
    if s < 0:
        l += 1
    else:
        r -= 1

print(a1, a2)
