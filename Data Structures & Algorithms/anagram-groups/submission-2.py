class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            key = [0]*26 #Creating a key 
            for c in s:
                key[ord(c)-ord('a')] += 1 # ord to get the ascii for character
                # +=1 beacuse to get the loaction in array
            out[tuple(key)].append(s)
        print(list(out.values()))
        return list(out.values())
