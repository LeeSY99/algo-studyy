class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        open = []
        close = []
        result = ""
        for c in s:
            if c == '(':
                open.append(c)
            elif c == ')':
                if len(open) > len(close):
                    close.append(c)
        open_count = 0
        for c in s:
            if c == '(':
                if close:
                    result += c
                    open_count += 1
                    close.pop()
            elif c == ')':
                if open and open_count > 0:
                    result += c
                    open_count -= 1
                    open.pop()
            else:
                result += c
        return result

                
        