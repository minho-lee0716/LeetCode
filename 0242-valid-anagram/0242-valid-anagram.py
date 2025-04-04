# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         s, t = sorted(s), sorted(t)
#         for i in range(len(s)):
#             if s[i] != t[i]:
#                 return False
#         return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         temp = []
#         for char in s:
#             if char in temp:
#                 continue
#             if s.count(char) != t.count(char):
#                 return False
#             temp.append(char)
#         return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        while (len(s) != 0):
            curr = s[0]
            if s.count(curr) != t.count(curr):
                return False
            s, t = s.replace(curr, ''), t.replace(curr, '')
            if len(s) != len(t):
                return False
        return True