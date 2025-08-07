n = int(input())

left = 0
right = 10**9 + 1


def check(num):
    return num - num//3 - num//5 + num//15

while left<=right:
    mid = (left + right) // 2
    if check(mid) < n:
        left = mid +1
    elif check(mid) > n:
        right = mid-1
    else:
        print(mid)
        break

    