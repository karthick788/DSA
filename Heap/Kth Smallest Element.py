class Solution:
    def kthSmallest(self, nums, k):
        h = []
        for i in nums:
            heapq.heappush(h,-i)
            print(h)
            if len(h) > k:
                heapq.heappop(h)
                print(h)
        return -h[0]
        
