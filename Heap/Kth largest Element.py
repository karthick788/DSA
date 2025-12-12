class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            heapq.heappush(h,i)
            print(h)
            if len(h) > k:
                heapq.heappop(h)
                print(h)
        return h[0]