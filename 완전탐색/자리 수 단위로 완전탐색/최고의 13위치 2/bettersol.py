n=int(input())

coins=[list(map(int,input().split())) for _ in range(n)]

max_coin=0
for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                if i==k and abs(j-l)<=2:continue
                #같은줄이고 j와l의 차기 2보다 작으면 겹침
                coin1=coins[i][j]+coins[i][j+1]+coins[i][j+2]
                coin2=coins[k][l]+coins[k][l+1]+coins[k][l+2]
                max_coin=max(max_coin,coin1+coin2)

print(max_coin)