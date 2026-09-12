class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for ch in s:
            s_dict[ch] += 1
        
        for ch in t:
            s_dict[ch] -= 1

 
        for key in s_dict.keys():
            if s_dict[key] != 0:
                return False
        return True
        