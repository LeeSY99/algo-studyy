string = input()
boom = list(input())

k = len(boom)
stack = []
for s in string:
    stack.append(s)
    if stack[len(stack) - k: len(stack)] == boom:
        for _ in range(k):
            stack.pop()

if stack:
    print(*stack, sep = '')
else:
    print("FRULA")


