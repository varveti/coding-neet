class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ref = {}
        for char in s:
            if char in ref:
                ref[char] += 1
            else:
                ref[char] = 1
        
        for char in t:
            if char not in ref:
                return False
            else:
                ref[char] -= 1

        for key, value in ref.items():
            if value > 0:
                return False
        print(ref)
        return True