n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def is_sub():
    i = 0
    for j in range(m):
        while i<n:
            if B[j] == A[i]:
                break
            i += 1
        if i == n:
            return 'No'
    
    return 'Yes'

print(is_sub())
