x,y=map(int,input().split())

count=0
for number in range(x,y+1):
    number=str(number)
    is_pal=True
    for i in range(len(number)//2):
        if number[i]!=number[len(number)-i-1]:
            is_pal=False
            break
    if is_pal:
        count+=1

print(count)