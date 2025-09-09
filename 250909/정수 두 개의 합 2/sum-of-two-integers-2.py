n,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
ans = 0
j = n-1

for i in range(n):
    while i<j and arr[i] + arr[j] > k:
        j -= 1

    if i == j: break

    ans += j-i
    

print(ans)
    