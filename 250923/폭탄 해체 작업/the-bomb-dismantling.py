
n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[1], -x[0]))
# print(arr)
now = 0
score = 0

for i in range(n):
    if arr[i][1] > now:
        now = arr[i][1]
        score += arr[i][0]

print(score)