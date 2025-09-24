from functools import cmp_to_key
n = int(input())
arr = [input() for _ in range(n)]

def compare(x,y):
    a = x+y
    b = y+x
    a_score = 0
    a_cnt = 0
    b_score = 0
    b_cnt = 0
    for i in range(len(a)):
        if a[i] == '(':
            a_cnt += 1
        else:
            a_score += a_cnt

        if b[i] == '(':
            b_cnt += 1
        else:
            b_score += b_cnt

    if a_score < b_score:
        return 1
    if a_score > b_score:
        return -1
    return 0

arr.sort(key = cmp_to_key(compare))
# print(arr)
ans = 0
cnt = 0
for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] == '(':
            cnt+=1
        else:
            ans += cnt

print(ans)