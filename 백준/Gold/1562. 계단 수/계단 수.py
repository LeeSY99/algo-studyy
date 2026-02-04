n = int(input())
MOD = 1000000000
all_use = (1<<10) - 1
def solve():
    if n < 10:
        print(0)
        return

    dp = [[0] * (1<<10) for _ in range(10)]

    # 초기화 1~10돌면서 d로 시작하는 수
    for d in range(1, 10):
        dp[d][1<<d] = 1

    for _ in range(1,n):
        ndp = [[0] * (1 << 10) for _ in range(10)]
        for d in range(10):
            row = dp[d]
            if d > 0:
                to = d-1
                bit = 1 << to
                nrow = ndp[to]
                for mask, val in enumerate(row):
                    if val:
                        nm = mask|bit
                        nrow[nm] = (nrow[nm] + val) % MOD
            if d < 9:
                to = d + 1
                bit = 1 << to
                nrow = ndp[to]
                for mask, val in enumerate(row):
                    if val:
                        nm = mask|bit
                        nrow[nm] = (nrow[nm] + val) % MOD
        dp = ndp

    ans = 0
    for d in range(10):
        ans = (ans + dp[d][all_use])% MOD
    print(ans)
solve()

