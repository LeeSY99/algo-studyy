n = int(input())
classes = []
for _ in range(n):
    s,e = map(int, input().split())
    classes.append((s,e))

classes.sort(key = lambda x: x[1])

count = 0
last_end = 0
# print(classes)
for start, end in classes:
    if start >= last_end:
        last_end = end
        count+=1

print(count)