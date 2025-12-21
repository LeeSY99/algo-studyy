s = input()
prec = {
    '+':1,
    '-':1,
    '*':2,
    '/':2
}
stack =[]
out = []

for ch in s:
    if 'A' <= ch <= 'Z':
        out.append(ch)
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            out.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1] != '(' and prec[stack[-1]] >= prec[ch]:
            out.append(stack.pop())
        stack.append(ch)


while stack:
    out.append(stack.pop())

print(''.join(out))