n = int(input())

arr1 = list(input())
arr2 = list(input())

start = False
count = 0
for i in range(n):
    if not start and arr1[i] != arr2[2]:
        start = True
        count +=1
        
    if start and arr1[i] == arr2[2]:
        start = False

print(count)