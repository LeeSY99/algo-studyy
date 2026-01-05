string1 = input()
string2 = input()

n = len(string1)
m = len(string2)
ans = []
dp = [[0] * (m+1) for _ in range(n+1)]
count = 1



for i in range(1,n+1):
    for j in range(1,m+1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
            # if dp[i][j] == count:
            #     count += 1
            #     ans.append(string2[j])
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

# for d in dp:
#     print(*d)

l = dp[n][m]
print(l)

if l != 0:
    i,j = n,m
    ans = []
    while i>0 and j>0:
        if string1[i-1] == string2[j-1]:
            ans.append(string1[i-1])
            i-=1
            j-=1
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                i-=1
            else:
                j-=1

    ans.reverse()
    print(''.join(ans))