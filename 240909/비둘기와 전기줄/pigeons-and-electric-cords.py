n=int(input())

bird=[0]*(n+1)
count=[0]*(n+1)
trace=[False]*(n+1)

for _ in range(n):
    bird_num, loc = map(int,input().split())
    if trace[bird_num]:
        if bird[bird_num] != loc:
            count[bird_num]+=1
            bird[bird_num] = loc
    else:
        trace[bird_num] = True
        bird[bird_num]=loc

print(sum(count))