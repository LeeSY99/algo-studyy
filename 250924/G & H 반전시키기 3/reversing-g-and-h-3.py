n = int(input())
before = list(input())
after = list(input())

cnt = 0
start = 0
for i in range(n):
    if not start and before[i] != after[i]:
        start = i
        cnt+=1
    if start and (before[i] == after[i] or i-start == 3):
        start = 0

print(cnt)