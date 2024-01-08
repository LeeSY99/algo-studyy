n=int(input())
arr=list(map(int,input().split()))

def gcd(a,b):
    if b==0:
        return a
    if a>b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a)
    
def lcm(a,b):
    return a*b//gcd(a,b)

def fun(n):
    if n==0:
        return arr[0]
    return lcm(arr[n],fun(n-1))

print(fun(n-1))
#O(n^2)