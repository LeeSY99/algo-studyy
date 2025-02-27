A = input()

# Please write your code here.

import sys
ans= sys.maxsize
A=list(A)
for i in range(len(A)):
    A.insert(0,A.pop())
    count=1
    nowchar=A[0]
    rle = ''
    for j in range(1,len(A)):
        if A[j] != nowchar:
            rle+=nowchar
            rle+=str(count)
            nowchar=A[j]
            count=1
        else:
            count+=1
    rle+=nowchar
    rle+=str(count)
    ans = min(ans,len(rle))
    # print(rle)
print(ans)

        






