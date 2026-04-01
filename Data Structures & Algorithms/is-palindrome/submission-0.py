class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s) 

        def is_alphanumeric(char):
            ord_char = ord(char)
            return ord('a') <= ord_char <= ord('z') or ord('A') <= ord_char <= ord('Z') or ord('0') <= ord_char <= ord('9')

        left = 0
        right = n - 1

        while left < right:
            while left < right and not is_alphanumeric(s[left]):
                left += 1
            while left < right and not is_alphanumeric(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
        
            left += 1
            right -= 1

        return True