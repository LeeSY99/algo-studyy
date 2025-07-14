n,m = map(int,input().split())

mydict = dict()
mydict2 = dict()

for i in range(1, n+1):
    alpha = input()
    mydict[alpha] = i
    mydict2[i] = alpha

for _ in range(m):
    k = input()
    if k in mydict:
        print(mydict[k])
    else:
        print(mydict2[int(k)])
        