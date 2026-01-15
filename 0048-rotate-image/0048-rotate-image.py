class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for l in range((n//2)+1):
            for _ in range(n-2*l-1):
                temp = matrix[l][l]
                max_j = n-l-1
                print(l, max_j)

                for i in range(l, max_j):
                    matrix[i][l] = matrix[i+1][l]
                for j in range(l, max_j):
                    matrix[max_j][j] = matrix[max_j][j+1]
                for i in range(max_j, l, -1):
                    matrix[i][max_j] = matrix[i-1][max_j]
                for j in range(max_j, l, -1):
                    matrix[l][j] = matrix[l][j-1]
                if l != max_j:
                    matrix[l][l+1] = temp
            