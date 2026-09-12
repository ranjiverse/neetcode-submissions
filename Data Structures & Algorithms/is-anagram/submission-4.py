class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]] += 1
            s_dict[t[i]] -= 1

        for key in s_dict.keys():
            if s_dict[key] != 0:
                return False
        return True
        