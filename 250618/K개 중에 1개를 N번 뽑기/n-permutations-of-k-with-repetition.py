k, n = map(int, input().split())


a=[]

def print_answer():
    print(*a)

def choose(count):
    if count==n:
        print_answer()
        return

    for i in range(1, k+1):
        a.append(i)
        choose(count+1)
        a.pop()


choose(0)