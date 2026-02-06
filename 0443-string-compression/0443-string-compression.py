class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0
        read = 0

        while read < n:
            ch = chars[read]
            count = 0

            while read < n and chars[read] == ch:
                read += 1
                count += 1
            
            chars[write] = ch
            write += 1

            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1

        del chars[write:]

                



