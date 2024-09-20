n=int(input())

blocks=[int(input()) for _ in range(n)]

for_block=int(sum(blocks)/n)

ans=0
for i in range(n):
    ans+=(abs(for_block-blocks[i]))

print(ans//2)