n=int(input())

bird=[0]*(11)
count=[0]*(11)
trace=[False]*(11)

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