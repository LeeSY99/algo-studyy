n = int(input())


def solve():
    p = []
    def backtrack(count):
        nonlocal p
        if count == n:
            if check():
                for num in p:
                    print(num, end = '')   
                quit() 
            return

        for i in range(4,7):
            p.append(i)
            backtrack(count+1)
            p.pop()

    def check():
        for i in range(n):
            for j in range(i+1, n):
                gap = j-i
                if gap > n-j:
                    continue
                count = 0
                for k in range(gap):
                    if p[i+k] == p[j+k]:
                        count+=1
                if count == gap:
                    return False
        return True

    a = backtrack(0)
    # for num in a:
    #     print(num, end = '')

solve()

