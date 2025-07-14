n,m = map(int,input().split())

mydict = dict()

for i in range(1, n+1):
    alpha = input()
    mydict[alpha] = str(i)

for _ in range(m):
    k = input()
    if k in mydict:
        print(mydict[k])
    else:
        for key, value in mydict.items():
            if value == k:
                print(key)