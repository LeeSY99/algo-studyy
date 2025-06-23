n = int(input())
p = []

def backtrack(count):
    # global p
    if count == n:
        for num in p:
            print(num, end = '')   
        quit() 
    
    for i in range(4,7):
        p.append(i)
        if check():
            backtrack(count+1)  
        p.pop()

def check():
    l = len(p)
    for gap in range(1,l//2+1):
        for i in range(l - 2 * gap+1):
            if p[i:i+gap] == p[i+gap:i+2*gap]:
                return False
    return True

backtrack(0)

