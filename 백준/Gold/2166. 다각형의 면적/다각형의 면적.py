n = int(input())
x = []
y = []
for _ in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)

ans = 0
for i in range(n):
    ans += x[i] * y[(i+1)%n]

for i in range(n-1,-1,-1):
    ans -= x[i] * y[(i-1)%n]

ans = abs(ans)/2

print(f'{ans:.1f}')