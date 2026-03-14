class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        visited = {}
        bulls = 0
        cows = 0

        n = len(secret)
        for i in range(n):
            num1 = int(secret[i])
            num2 = int(guess[i])
            if num1 == num2:
                bulls += 1
            else:
                visited[num1] = visited.get(num1, 0) + 1

        print(visited)
        for i in range(n):
            num1 = int(secret[i])
            num2 = int(guess[i])
            if num1 == num2:
                continue
            else:
                if visited.get(num2, 0) != 0:
                    cows+=1
                    visited[num2] = visited[num2] - 1
                    

        return f"{bulls}A{cows}B"
        