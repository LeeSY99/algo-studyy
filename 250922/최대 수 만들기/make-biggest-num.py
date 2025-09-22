from functools import cmp_to_key
n = int(input())
arr = [input() for _ in range(n)]
def compare(x,y):
    if int(x)* 10**len(y) + int(y) > int(y) *  10**len(x) + int(x):
        return -1
    if int(x)* 10**len(y) + int(y) < int(y) *  10**len(x) + int(x):
        return 1
    return 0

arr.sort(key = cmp_to_key(compare))

ans = ''
for a in arr:
    ans += a

print(ans)
