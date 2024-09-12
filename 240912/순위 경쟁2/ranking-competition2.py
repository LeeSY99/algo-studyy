n=int(input())
a,b=0,0
prize='AB'
count=0
for _ in range(n):
    p, s = input().split()
    if p=='A':
        a+=int(s)
    else:
        b+=int(s)
    
    if a==b:
        win='AB'
    elif a>b:
        win='A'
    elif a<b:
        win='B'
    if prize!=win:
        count+=1
        prize=win
print(count)