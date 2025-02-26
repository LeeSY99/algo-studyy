n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Write your code here!
n=n-1
m=m-1

def up(line,a, right):
    for l in range(line,0,-1):
        right = not right       #다음 방향 정함
        keep = False
        for i in range(m+1):
            if a[l][i] == a[l-1][i]:
                keep = True
                break
        if not keep:
            return
        spread(right, l-1,a)

def down(line,a,right):
    for l in range(line,n):
        right = not right
        keep = False
        for i in range(m+1):
            if a[l][i] == a[l+1][i]:
                keep = True
                break
        if not keep:
            return
        spread(right, l+1, a)

def spread(right,l,a):
    if right:
        temp = a[l][0]
        for i in range(m):
            a[l][i] = a[l][i+1]
        a[l][m] = temp
    else:
        temp = a[l][m]
        for i in range(m,-1,-1):
            a[l][i] = a[l][i-1]
        a[l][0] = temp
            


for line, direction in winds:
    if direction == 'L':
        right = False
    else:
        right = True
    spread(right, line-1, a)
    up(line-1, a ,right)
    down(line-1,a,right)
    
for lst in a:
    print(*lst)