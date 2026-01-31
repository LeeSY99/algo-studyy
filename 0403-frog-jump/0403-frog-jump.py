class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) < 2:
            return True
        if stones[1] != 1:
            return False

        # 가지치기(정석에 자주 포함됨)
        for i in range(1, len(stones)):
            if stones[i] - stones[i-1] > i:
                return False

        stones_set = set(stones)
        dp = defaultdict(set)
        dp[0].add(0)
        last = stones[-1]

        for pos in stones:                 # 반드시 "리스트"로 순회(정렬 순서 유지)
            for k in dp[pos]:
                for nk in (k-1, k, k+1):
                    if nk <= 0:
                        continue
                    npos = pos + nk
                    if npos == last:
                        return True
                    if npos in stones_set:
                        dp[npos].add(nk)

        return False