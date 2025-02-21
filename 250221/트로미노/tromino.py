n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
# ㄱ자 블록

ans=0
def r_block(lst,r,l):
    sum1,sum2,sum3,sum4=0,0,0,0
    if 0 <= r <=n-2 and 0<=l<=m-2:
        block_sum = lst[r][l] + lst[r][l+1] + lst[r+1][l] + lst[r+1][l+1]
        sum1=block_sum - lst[r][l]
        sum2=block_sum - lst[r][l+1]
        sum3=block_sum - lst[r+1][l]
        sum4=block_sum - lst[r+1][l+1]
    return max(sum1,sum2,sum3,sum4)

# 직선 블록
def l_block(lst,r,l):
    block_sum1,block_sum2=0,0
    if  0 <= r <n and 0 <= l <m-2:
        block_sum1 = lst[r][l] + lst[r][l+1] + lst[r][l+2]
    if  0 <= r <n-2 and 0 <= l <m:
        block_sum2 = lst[r][l] + lst[r+1][l] + lst[r+2][l]
    return max(block_sum1,block_sum2)


for i in range(n):
    for j in range(m):
        ans=max(ans,r_block(nums, i, j))
        ans=max(ans,l_block(nums, i, j))

print(ans)



