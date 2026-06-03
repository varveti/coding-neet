class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        ref_str = strs[0]
        for i in range(len(ref_str)):
            for s in strs:
                if i == len(s) or s[i] != ref_str[i]:
                    return out
            out += ref_str[i]
        return out