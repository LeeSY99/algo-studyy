class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = 1
        alpha_index = {}

        for o in order:
            alpha_index[o] = index
            index += 1

        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            n = len(word1)
            m = len(word2)
            for j in range(min(n,m)):
                if alpha_index[word1[j]] > alpha_index[word2[j]]:
                    return False
                elif alpha_index[word1[j]] == alpha_index[word2[j]]:
                    if j == min(n,m)-1 and n > m:
                        return False
                    continue
                else:
                    break
        
        return True

        