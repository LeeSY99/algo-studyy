class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        n = len(s)
        stack = []
        answer = ''

        for i in range(n):
            if s[i] == '[':
                stack.append(s[i])
                continue
            if 'a' <= s[i] <= 'z':
                stack.append(s[i])
                continue
            if s[i] == ']':
                sub_word = []
                while stack[-1] != '[':
                    sub_word.append(stack.pop())
                mini_word = ''
                for j in range(len(sub_word)-1,-1,-1):
                    mini_word += sub_word[j]
                stack.pop()
                time = 0
                ten = 0

                while stack and isinstance(stack[-1], int):
                    time += stack.pop() * (10**ten)
                    ten += 1

                stack.append(mini_word * time)
                print(stack)
                continue
            if  0 <= int(s[i]) <= 9:
                stack.append(int(s[i]))
                continue

        for word in stack:
            answer += word

        return answer

