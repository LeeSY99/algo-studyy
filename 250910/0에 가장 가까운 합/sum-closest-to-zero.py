n = int(input())

arr= list(map(int, input().split()))

ans = float('inf')
from sortedcontainers import SortedSet
ss = SortedSet(arr)
n = len(ss)
j = n-1
# print(ss)
for i in range(n):
    while i<j and abs(ss[i] + ss[j]) < ans:
        ans = abs(ss[i] + ss[j])
        j-=1

print(ans)