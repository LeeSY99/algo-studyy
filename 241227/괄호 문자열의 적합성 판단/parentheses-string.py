string = input()

mystack=[]

for i in range(len(string)):
    if string[i]=='(':
        mystack.append('(')
    else:
        if len(mystack)==0:
            print('No')
            quit()
        mystack.pop()

if len(mystack)==0:
    print('Yes')
else:
    print('No')
