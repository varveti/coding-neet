class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ref = {}
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}
        for i in range(len(t)):
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
        
        return s_map == t_map