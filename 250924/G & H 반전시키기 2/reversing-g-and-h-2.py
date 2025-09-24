n = int(input())
before = list(input())
after = list(input())
# alpha = {'H': 0, 'G':1}
cnt = 0
for i in range(n-1,-1,-1):
    if before[i] != after[i]:
        cnt+=1
        for j in range(i+1):
            if before[j] == 'H':
                before[j] = 'G'
            else:
                before[j] = 'H'

# for i in range(n):
#     if before[i] != after[i]:
#         cnt = -1

print(cnt)