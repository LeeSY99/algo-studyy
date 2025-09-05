n = int(input())

nums = list(map(int, input().split()))

L = [0] * n
R = [0] * n

total = sum(nums)
if total %4 != 0:
    print(0)
    quit()

target_sum = total //4

sum_val = nums[0]
cnt = 1 if sum_val == target_sum else 0

for i in range(1,n):
    sum_val += nums[i]
    if sum_val == 2* target_sum:
        L[i] = cnt
    if sum_val == target_sum:
        cnt += 1

sum_val = nums[n-1]
cnt = 1 if sum_val == target_sum else 0

for i in range(n-2,-1,-1):
    sum_val += nums[i]
    if sum_val == 2*target_sum:
        R[i] = cnt

    if sum_val == target_sum:
        cnt += 1

# print(L)
# print(R)

ans = 0
for i in range(1,n-1):
    ans += L[i] * R[i+1]
print(ans)


