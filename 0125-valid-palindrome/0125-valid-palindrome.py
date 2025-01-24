class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()]).lower()
        size = len(s)
        return s[:size//2] == s[size//2:][::-1] if size % 2 == 0 else s[:size//2] == s[size//2 + 1:][::-1]
