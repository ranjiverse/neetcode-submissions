class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        l = 0
        max_freq = 0
        res = 0

        for r in range(len(s)):
            char_freq[s[r]] += 1
            max_freq = max(max_freq, char_freq[s[r]])
            window_size = r - l + 1
            if k < window_size - max_freq:
                char_freq[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res

            



        