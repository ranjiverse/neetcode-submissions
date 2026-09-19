class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        res = [] 

        for ch in s:
            if ch not in pairs.keys():
                res.append(ch)
            elif res and pairs[ch] == res[-1]:
                res.pop(-1)
            else :
                res.append(ch)
        if len(res) > 0 :
            return False
        return True 

        