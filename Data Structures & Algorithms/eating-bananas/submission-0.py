class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = max(piles)
        k_min = 1
        k = k_max
 

        while k_min <= k_max:
            k_mid = (k_min + k_max) // 2
            total_hrs = 0
            for p in piles:
                total_hrs += math.ceil(p/k_mid)
            if total_hrs > h:
                k_min = k_mid + 1
            elif total_hrs <= h:
                k_max = k_mid - 1
                k = min(k, k_mid)
        
        return k

            

        