n,m = map(int, input().split())
arr= [0] + list(map(int, input().split()))
# arr_sum = [0] * (n+1)
# for i in range(1,n+1):
#     arr_sum[i] = arr_sum[i-1] + arr[i]
offset = 20


#dp[i][j]: i번쨰 수까지 고려 합이 j -> 가지수
dp = [[0] * (41) for _ in range(n+1)]
# for i in range(41):
#     dp[0][i] = 0
def in_range(a):
    return 0<=a<=40

dp[0][offset] = 1  
for i in range(1,n+1):
    x = arr[i]
    for j in range(41):
        a = j-x
        b = j+x
        if in_range(a):
            dp[i][j] += dp[i - 1][a]
        if in_range(b):
            dp[i][j] += dp[i - 1][b]
        

# for d in dp:
#     print(*d)
    
print(dp[n][m+offset])