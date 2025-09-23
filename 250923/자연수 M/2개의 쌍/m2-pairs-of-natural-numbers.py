n = int(input())

arr = []
for _ in range(n):
    x,y = map(int, input().split())
    arr += [y]*x

arr.sort()
ans = float('inf')
for i in range(len(arr)//2):
    ans = min(ans, arr[-1-i] + arr[i])

# print(arr)
print(ans)