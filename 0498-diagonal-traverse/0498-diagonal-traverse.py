class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n = len(mat)
        m = len(mat[0])
        max_val = n-1 + m-1

        for d in range(max_val + 1):
            diag = []
            r_start = max(0, d - m + 1)
            r_end = min(n-1, d)

            for r in range(r_start, r_end + 1):
                c = d-r
                diag.append(mat[r][c])

            if d%2 == 0:
                diag.reverse()
            ans.extend(diag)

        return ans
        