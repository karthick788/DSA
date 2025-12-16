class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = Counter(nums)

        h = []
        for i,j in ans.items():
            heapq.heappush(h,(j,i))
            if len(h) > k:
                heapq.heappop(h)
    
        return [val for i,val in h]