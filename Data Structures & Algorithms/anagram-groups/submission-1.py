class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')] += 1
            out[tuple(key)].append(s)
        print(list(out.values()))
        return list(out.values())
