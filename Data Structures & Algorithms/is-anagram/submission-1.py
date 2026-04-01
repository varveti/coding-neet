class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ref = Counter(s)
        # print(ref)
        # for st in t:
        #     ref[st] -= 1
        return Counter(s) == Counter(t)
        