s = input().strip()
arr = [ord(c.lower()) - ord('a') for c in s if c.isalpha()]
n = len(arr)

if n == 0:
    print(0)
else:
    best = 1
    cur_l = 0
    for r in range(1, n):
        if arr[r] != arr[r-1] + 1:
            cur_l = r
        best = max(best, r - cur_l + 1)
    print(best)
