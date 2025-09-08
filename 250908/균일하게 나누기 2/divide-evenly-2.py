n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort()

#i번째 점까지 각 x,y의 최대값
X = [0]*1001
Y = [0]*1001
# X[0] = points[0][0]
# Y[0] = points[0][1]

''' y갑을 정해놓고 x값을 왼쪽으로 보내면서 값을 비교하기'''

ans = float('inf')
for b in range(0, 1001, 2):
    cnt = [0] * 5 #사분면 개수
    for x, y in points: #초기에는 x가 다 0보다 큼, 1,4분면에만
        if y > b:
            cnt[1] +=1
        else:
            cnt[4] += 1
    
    #이제 x값에 따라 이동
    for i in range(n):
        if i==0 or points[i][0] != points[i-1][0]: #x값이 바뀔떄 값 갱신
            ans = min(ans, max(cnt))
        
        x,y = points[i]
        if y>b:
            cnt[1] -= 1
            cnt[2] += 1
        else:
            cnt[4] -= 1
            cnt[3] += 1

print(ans)

