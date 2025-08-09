a = list(input())
n = len(a)

r = [0] * (n)

for i in range(n-2,-1,-1):
    if a[i] == ')' and a[i] == a[i+1]:
        r[i] = r[i+1]+1
    else:
        r[i] = r[i+1]

ans = 0
for i in range(n-2):
    if a[i] == '(' and a[i] == a[i+1]:
        ans += r[i+2]

print(ans)
    