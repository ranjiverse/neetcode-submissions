class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """  
        res = [[-1, -1, 2], [-1, -1, 2], [-1,0,1]]
        Input = [-1,0,1,2,-1,-4]
        Sorted = [-4,-1,-1,0,1,2]

        -1 = -1 + 2
        -1 = -1 + 2
    
        
        Take one number and run two pointer algo on rest of the array 
        to find out how many triplets can be formed

        Then we need to handle duplicates

        time complexity will be = O(n)2 , O(n) for loop through every element
        and O(n) for every two pointer algorithm
        """ 
        res = []
        nums.sort()
        length = len(nums)

        for i in range(length):
            if nums[i] > 0 :
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r= length-1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append([nums[i],nums[l], nums[r]])
                    l = l + 1
                    while l < r and nums[l] == nums[l-1]:
                        l = l + 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r = r - 1
                else:
                    l = l + 1

        return res

