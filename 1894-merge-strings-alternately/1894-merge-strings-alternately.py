class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        w1, w2 = list(word1), list(word2)
        while len(result) < (len(word1) + len(word2)):
            if not w1:
                result += ''.join(w2)
                break
            result += w1.pop(0)

            if not w2:
                result += ''.join(w1)
                break
            result += w2.pop(0)

        return result