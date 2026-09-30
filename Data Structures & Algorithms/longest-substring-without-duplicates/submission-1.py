class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        global_max = 0
        l = 0

        for r in range(len(s)):
            ch = s[r]

            if ch in char_map  and char_map[ch] >= l:
                l = char_map[ch] + 1

            char_map[ch] = r
            global_max = max(global_max, (r-l+1))

        return global_max


            
        