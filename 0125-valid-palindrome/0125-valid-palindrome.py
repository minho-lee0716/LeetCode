class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()]).lower()
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                return False
        return True
