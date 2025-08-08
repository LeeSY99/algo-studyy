n,k,b = map(int, input().split())

arr = [0] * (n+1)
for _ in range(b):
    a = int(input())
    arr[a] = 1

''' 1~n숫자 b개 빠짐 연속한 k개 숫자들이 최소 한 세트는 존재하려 할때 
b개의 숫자 중 추가해야하는 숫자 개수의 최솟값'''

#O(n)


prefix_sum = [0] * (n+1)
for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

import sys
ans = sys.maxsize
for i in range(k, n+1):
    ans = min(ans, prefix_sum[i]-prefix_sum[i-k+1])

print(ans)


