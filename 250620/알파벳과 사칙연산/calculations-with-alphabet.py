expression = input()

alpha ={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
op = ['+','-','*']


import sys
def max_result():
    ans = -sys.maxsize
    nums = []
    def backtrack(count):
        nonlocal ans
        if count == 6:
            result = 0
            to_calc=['+']
            for e in expression:
                if e in alpha:
                    c = to_calc.pop()
                    if c == '+':
                        result += nums[alpha[e]]
                    elif c == '*':
                        result *= nums[alpha[e]]
                    else:
                        result -= nums[alpha[e]]
                if e in op:
                    to_calc.append(e)
            ans = max(ans, result)
            return

        for i in range(1,5):
            nums.append(i)
            backtrack(count+1)
            nums.pop()
    backtrack(0)
    return ans

print(max_result())
            


