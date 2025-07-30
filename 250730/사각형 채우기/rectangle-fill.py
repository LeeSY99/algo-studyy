n = int(input())

rect = [0] *(n+1)

for i in range(1,n+1):
    if i==1:
        rect[i] = 1
    elif i==2:
        rect[i] = 2
    else:
        rect[i] = rect[i-2] + rect[i-1]

print(rect[n]%10007)