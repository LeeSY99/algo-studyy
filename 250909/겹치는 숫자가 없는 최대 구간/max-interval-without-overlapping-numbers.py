n = int(input())
arr = list(map(int, input().split()))

num_count = [0] * 100001

j = 0
ans = 0
for i in range(n):
    while j<n and num_count[arr[j]] < 1:
        num_count[arr[j]] += 1
        j+=1
    
    # if j == n:
    #     break

    # print(i,j)
    ans = max(ans, j-i)
    num_count[arr[i]] -= 1

print(ans)
    
