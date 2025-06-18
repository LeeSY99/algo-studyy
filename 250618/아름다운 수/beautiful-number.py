n = int(input())

ans = 0
num = []

def beautiful(count):
    if count == n:
        check()
        return

    for i in range(1,5):
        num.append(i)
        beautiful(count+1)
        num.pop()

def check():
    global ans
    index=0
    while index<n:
        first = num[index]
        if first > n-index:
            return 
        for i in range(first):
            if num[index + i] != first:
                return
        index += first
    ans+=1
    return

beautiful(0)
print(ans)

