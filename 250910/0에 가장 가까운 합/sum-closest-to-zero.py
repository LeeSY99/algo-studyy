n = int(input())

arr= list(map(int, input().split()))

ans = float('inf')
from sortedcontainers import SortedSet
ss = SortedSet(arr)
n = len(ss)
i = 0
j = n-1
# print(ss)
while i<j:
    s = ss[i] + ss[j]
    ans = min(ans, abs(s))
    if s < 0:
        i+=1
    else:
        j-=1

print(ans)