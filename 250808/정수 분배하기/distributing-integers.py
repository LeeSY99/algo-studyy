n,m = map(int, input().split())
k = 0
nums = []
ans = 0

for _ in range(n):
    a = int(input())
    nums.append(a)
left = 1
right = 100000

def is_possible(d):
    count = 0
    for num in nums:
        count += (num // d)

    if count >= m:
        return True

    return False

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid-1

print(ans)
