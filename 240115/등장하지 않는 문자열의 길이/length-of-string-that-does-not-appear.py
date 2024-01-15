n = int(input())
string = input()


for i in range(1,n+1):
    ok = False
    for j in range(n-i+1):
        substr=string[j:j+i]
        sub_count=0
        for k in range(n-len(substr)+1):
            if string[k:k+len(substr)]==substr:
                sub_count+=1
        if sub_count>=2:
            ok=True
            break     
    if not ok:
        print(i)
        break