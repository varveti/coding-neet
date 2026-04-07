class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            out[sorteds].append(s)
        print(out)
        print(list(out.values()))
        return (list(out.values()))