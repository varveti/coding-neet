class Solution:
    def isValid(self, s: str) -> bool:
        ref = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen:
                if ref and ref[-1] == closeToOpen[c]:
                    ref.pop()
                else:
                    return False
            else:
                ref.append(c)
        
        return True if not ref else False

