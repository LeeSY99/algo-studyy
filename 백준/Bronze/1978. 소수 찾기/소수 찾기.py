n = int(input())
nums = list(map(int, input().split()))

import math
ans = 0
for num in nums:
    is_prime = True
    if num == 1:
        continue
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        ans += 1
print(ans)


