n,m=map(int,input().split())


nums = [(a, b) if a >= b else (b, a) for _ in range(m) for a, b in [map(int, input().split())]]
count={}
for t in nums:
    try:
        count[t]+=1
    except KeyError:
        count[t]=1
print(max(count.values()))