class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ref = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter not in ref:
                ref[letter] = 1
            else:
                ref[letter] += 1

        for letter in t:
            if letter not in ref or ref[letter] <= 0:
                return False
            ref[letter] -= 1

        # for value in ref.values():
        #     if value != 0:
        #         return False
        return True