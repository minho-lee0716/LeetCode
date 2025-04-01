class Solution:
    def reverseVowels(self, s: str) -> str:
        alter, temp, gather, result = None, [], [], ""
        for char in s:
            if char in ['A','E','I','O','U','a','e','i','o','u']:
                temp.append(alter)
                gather.append(char)
            else:
                temp.append(char)

        for t in temp:
            result += gather.pop() if t is alter else t

        return result
