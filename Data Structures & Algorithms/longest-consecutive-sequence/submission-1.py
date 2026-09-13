class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        l = len(hash_set)
        res = 0
        for num in hash_set:
            if num-1 not in hash_set:
                cur_streak = 1
                while num + cur_streak in hash_set:
                    cur_streak +=1 
                res = max(res, cur_streak)
        return res
                    
                    
