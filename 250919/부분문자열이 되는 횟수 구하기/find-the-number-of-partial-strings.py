A = list(input())
B = input()
order = list(map(int, input().split()))

left = 0
right = len(B)-1

def check(m):
    removed = [False] * len(A)
    for i in range(m):
        removed[order[i]-1] = True
    
    i = 0
    for j in range(len(A)):
        if removed[j]:
            continue
        if i < len(B) and A[j] == B[i]:
            i+=1
            if i == len(B):
                return True
    return i == len(B)

ans =0      

while left <= right:
    mid = (left+ right) // 2
    if check(mid):
        ans = mid+1
        left = mid + 1
    else:
        right = mid - 1

print(ans)
        
