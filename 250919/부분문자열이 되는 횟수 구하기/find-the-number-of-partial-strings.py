A = list(input())
B = input()
order = list(map(int, input().split()))

left = 0
right = len(B)-1

def check(m):
    new_A = A[:]
    for i in range(m+1):
        new_A[order[i]] = None
    new_str = ''
    for i in range(m+1):
        if new_A[i] == None:
            continue
        new_str += new_A[i]

    if len(new_str) < len(B):
        return False
    
    i = j = 0
    while j<len(new_str) and i<len(B):
        if B[i] == new_str[j]:
            i+=1
            cnt+=1
        j+=1
    if i == len(B):
        return True
    return False
    
  
ans =0      

while left <= right:
    mid = (left+ right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
    ans = max(ans, mid+1)

print(ans)
        
