class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        heap = []
        for key in d.keys():
            heapq.heappush(heap, (d[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for h in heap:
            res.append(h[1])
        return res


