n = int(input())

lines=[]
for i in range(n):
    a ,b = map(int, input().split())
    lines.append((a,b))

ans = 0

select=[]
def choose(a):
    global ans
    global lines
    if a == n:
        choosed=[]
        for i in range(n):
            if select[i] == 1:
                choosed.append(lines[i])
        count = check(choosed)
        ans = max(ans, count)
        return
    select.append(0)
    choose(a+1)
    select.pop()

    select.append(1)
    choose(a+1)
    select.pop()

def check(choosed):
    count = 0
    end = -1
    for a, b in choosed:
        if a>end:
            count+=1
            end = b
    return count        

choose(0)
print(ans)