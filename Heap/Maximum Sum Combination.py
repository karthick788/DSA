class Solution:
    def topKSumPairs(self, a, b, k):
        # code here
        a.sort()
        b.sort()
        n = len(a)
        
        heap = []
        heapq.heappush(heap,(-(a[n-1] + b[n-1]),n-1,n-1))
            
        visited = set()
        visited.add((n-1,n-1))
        ans = []
        
        while k > 0 and heap:
            k -= 1
            neg_sum,i,j = heapq.heappop(heap)
            curr_sum = -neg_sum
            ans.append(curr_sum)
            
            if i-1 >= 0:
                state = (i-1,j)
                if state not in visited:
                    visited.add(state)
                    heapq.heappush(heap,(-(a[i-1]+b[j]),i-1,j))
                    
            if j-1 >= 0:
                state = (i,j-1)
                if state not in visited:
                    visited.add(state)
                    heapq.heappush(heap,(-(a[i]+b[j-1]),i,j-1))
                    
        return ans
                
                