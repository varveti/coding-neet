class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        first = 0 
        last = len(s) - 1
        while first < last:
            if s[last].isalnum() and s[first].isalnum():
                if s[last] == s[first]:
                    first += 1
                    last -= 1
                else:
                    return False
            elif not s[first].isalnum():
                first += 1
            elif not s[last].isalnum():
                last -= 1
        return True
            