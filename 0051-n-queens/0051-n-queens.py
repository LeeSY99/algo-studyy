class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        chess = [['.'] * n for _ in range(n)]
        col = set()
        diag = set()
        revdiag = set()

        find(chess, result, 0, col, diag, revdiag)
        return result

def find(chess, result, y, col, diag, revdiag):
    if y == len(chess):
        temp = []
        for row in chess:
            temp.append("".join(row))
        result.append(temp)
        return

    for x in range(len(chess)):
        if isvalid(y,x,col,diag,revdiag):
            chess[y][x] = 'Q'
            col.add(x)
            diag.add(x+y)
            revdiag.add(x-y)

            find(chess, result, y+1, col, diag, revdiag)

            chess[y][x] = '.'
            col.remove(x)
            diag.remove(x+y)
            revdiag.remove(x-y)        


def isvalid(y,x,col, diag, revdiag):
    if x in col:
        return False
    if x+y in diag:
        return False
    if x-y in revdiag:
        return False
    return True
            

        