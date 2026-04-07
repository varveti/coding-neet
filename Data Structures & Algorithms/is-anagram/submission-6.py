class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First check the obvius conditions 
        # if len of both the stings are not equal then they are not anagrams
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT