n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

def same(lst):
    return all(x == lst[0] for x in lst)

ans=0
for i in range(n):
    lst1=nums[i]
    lst2=[a[i] for a in nums]

    for j in range(n-m+1):
        if same(lst1[j:j+m]):
            ans+=1
            break
    for j in range(n-m+1):
        if same(lst2[j:j+m]):
            ans+=1
            break


print(ans)

