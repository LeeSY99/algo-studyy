n,m=map(int,input().split())

field=[list(map(int,input().split())) for _ in range(n)]


def get_cost(k):
    return k*k+(k+1)*(k+1)

def get_gold(row,col,k):
    return sum([field[i][j] for i in range(n) for j in range(n) if abs(row - i) + abs(col - j) <= k])
#가장 거리가 먼 좌측상단과 우측하단을 커버하기 위해서 2(n-1)까지 커져야함
    
max_gold=0         
for r in range(n):
    for c in range(n):
        for k in range(2 * (n - 1) + 1):
            gold_sum=get_gold(r,c,k)
            if gold_sum*m>=get_cost(k):
                max_gold=max(max_gold,gold_sum)

print(max_gold)
