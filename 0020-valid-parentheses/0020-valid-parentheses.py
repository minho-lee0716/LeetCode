class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(":")", "{":"}", "[":"]"}
        for char in s:
            if char in mapping.keys():
                stack.append(char)

            elif not stack:
                return False

            elif char in mapping.values():
                if char != mapping[stack.pop()]:
                    return False

        return not stack