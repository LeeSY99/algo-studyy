ability=list(map(int,input().split()))

import sys
minab=sys.maxsize
for i in range(4):
    for j in range(i+1,5):

        for k in range(4):
            for l in range(k+1,5):
                if i==k or i==l or j==k or j==l:
                    continue
                sum1=ability[i]+ability[j]
                sum2=ability[k]+ability[l]
                sum3=sum(ability)-sum1-sum2

                if sum1==sum2 or sum1==sum3 or sum2==sum3:
                    break
                else:
                    minab=min(minab,abs(max(sum1,sum2,sum3)-min(sum1,sum2,sum3)))

if minab==sys.maxsize:
    print(-1)
else:
    print(minab)