import heapq
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        heap = []
        for v,w in zip(val,wt):
            heapq.heappush(heap,(-(v/w),v,w))
        
        cost = 0
        while heap and capacity > 0:
            ratio,value,weight = heapq.heappop(heap)
            r = -ratio
            
            if capacity == 0:
                break
            elif capacity >= weight:
                cost += value
                capacity -= weight
            else:
                cost += r*capacity
                capacity = 0
                
        return cost