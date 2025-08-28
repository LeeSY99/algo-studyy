a, b = map(int, input().split())

A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

A_B = set()
for elem in A:
    if not elem in B:
        A_B.add(elem)

B_A = set()
for elem in B:
    if not elem in A:
        B_A.add(elem)

print(len(set(list(A_B) + list(B_A))))
