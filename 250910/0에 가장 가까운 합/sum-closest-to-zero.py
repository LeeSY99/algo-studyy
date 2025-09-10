n = int(input())

arr= list(map(int, input().split()))

ans = float('inf')
from sortedcontainers import SortedSet
ss = SortedSet(arr)
n = len(ss)
j = n-1
for i in range(n):
    while i<j and abs(arr[i] - arr[j]) < ans:
        ans = abs(arr[i] - arr[j])
        j-=1

print(ans)