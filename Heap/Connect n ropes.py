import heapq
class Solution:
   def minCost(self, arr):
        h = []
        for i in arr:
            heapq.heappush(h,i)

        cost = 0
        while len(h) > 1:
            ans1 = heapq.heappop(h)
            ans2 = heapq.heappop(h)
            s = ans1+ans2
            cost += s
            heapq.heappush(h,s)
            
        return cost