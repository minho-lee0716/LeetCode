class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # result = ''
        # w1, w2 = list(word1), list(word2)
        # while len(result) < (len(word1) + len(word2)):
        #     if not w1:
        #         result += ''.join(w2)
        #         break
        #     result += w1.pop(0)

        #     if not w2:
        #         result += ''.join(w1)
        #         break
        #     result += w2.pop(0)
        # return result

        result = ''
        temp = min(len(word1), len(word2))
        for i in range(temp):
            result += word1[i]
            result += word2[i]

        result += word1[temp:]
        result += word2[temp:]
        return result