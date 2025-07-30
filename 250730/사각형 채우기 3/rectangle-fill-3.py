n = int(input())

rect = [1] *(n+1)
for i in range(1,n+1):
    if i==1:
        rect[i] = 2
    elif i == 2:
        rect[i] = 7
    else:
        a = 2*rect[i-1] + 3 * rect[i-2] 
        for j in range(i-3,-1,-1):
            a += 2*rect[j]
        rect[i] = a

print(rect[i] % 1000000007)