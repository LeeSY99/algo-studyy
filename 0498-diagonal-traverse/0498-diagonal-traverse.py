class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        n = len(mat)
        m = len(mat[0])
        max_val = n-1 + m-1

        for s in range(max_val + 1):
            if s % 2 == 0:
                for i in range(min(n-1, s),-1, -1):
                    j = s - i
                    if j >= m:
                        break
                    print(s,i,j)
                    result.append(mat[i][j])
            else:
                for j in range(min(m-1, s),-1,-1):
                    i = s-j
                    if i >= n:
                        break
                    print(s,i,j)
                    result.append(mat[i][j])
        return result
        