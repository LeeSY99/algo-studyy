n=int(input())
string=input()

def in_range(x):
    return 0<=x and x<n
for i in range(n):
    for j in range(n):
        ok=False
        if in_range(j+i+1):
            sub_string=string[j:j+i+1]
            if string.count(sub_string) >=2:
                ok=True
                break
    if not ok:
        print(i+1)
        break