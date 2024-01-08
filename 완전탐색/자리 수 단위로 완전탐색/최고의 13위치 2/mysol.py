n=int(input())

coins=[list(map(int,input().split())) for _ in range(n)]

max_coin=0
for i in range(n):
    for j in range(n-2):
        coin1=0
        coin1=coin1+ coins[i][j]+coins[i][j+1]+coins[i][j+2]
        if j>=n-5:
            for k in range(i+1,n):
                for l in range(n-2):
                    coin2=coin1+ coins[k][l]+coins[k][l+1]+coins[k][l+2]
                    max_coin=max(max_coin,coin2)
        else:
            for k in range(i,n):
                for l in range(j+3,n-2):
                    coin2=coin1+ coins[k][l]+coins[k][l+1]+coins[k][l+2]
                    max_coin=max(max_coin,coin2)


print(max_coin)