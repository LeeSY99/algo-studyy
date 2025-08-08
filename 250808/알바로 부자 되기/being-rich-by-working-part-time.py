''' n개의 알바 
일하는 시간 겹치지 않고 얻을 수 있는 돈 최대
'''

n = int(input())

alba_info = [(0,0,0)]
for _ in range(n):
    s,e,p = map(int, input().split())
    alba_info.append((s,e,p))
# print(alba_info)

dp = [[0,0,0] for _ in range(n+1)]
 
for i in range(1,n+1):
    for j in range(i):
        ns,ne,np = alba_info[i]
        ps,pe,pp = dp[j]
        if pe < ns:
            if pp + np > dp[i][2]:
                dp[i] = (ns,ne,pp+np)

ans = 0
# for d in dp:
    # print(*d)
for d in dp:
    ans = max(ans, d[2])

print(ans)