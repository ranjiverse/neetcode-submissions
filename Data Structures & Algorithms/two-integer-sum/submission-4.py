class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in d:
                return [d[diff], i]
            d[nums[i]] = i

        # for i in range(len(nums)):
            
        #      and d.get(diff)!=i :
        #         return [i, d[target-nums[i]]]

