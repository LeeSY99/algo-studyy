a = list(input())
n = len(a)

open_ = [0] * n
close_ = [0] * n

for i in range(n-1,0,-1):
    if a[i] == ')' and a[i-1] == a[i]:
        close_[i] += 1

for i in range(n-1):
    if a[i] == '(' and a[i] == a[i+1]:
        open_[i] += 1

# print(open_)
# print(close_)

print(sum(open_) * sum(close_))