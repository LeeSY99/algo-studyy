'''컨베이어 벨트 2*n 
시계방향으로 1초에 한칸씩'''

n, t = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]

for _ in range(t):
    temp1 = [belt[0][-1]]
    temp2 = [belt[1][-1]]
    belt1 = belt[0][:n-1]
    belt2 = belt[1][:n-1]
    belt[0] = temp2 + belt1
    belt[1] = temp1 + belt2 

for b in belt:
    print(*b)

