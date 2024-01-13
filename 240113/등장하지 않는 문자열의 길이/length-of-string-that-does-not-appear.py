n=int(input())
string=input()

for i in range(n):
    sub_string=string[0:i+1]
    if string.count(sub_string) <2:
        print(i+1)
        break