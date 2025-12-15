import heapq
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        h = []
        for idx,val in enumerate(arr):
            heapq.heappush(h,(val,idx))

        rank = 0
        last_val = float('inf')

        while h:
            val,idx = heapq.heappop(h)
            if last_val != val:
                rank += 1
                last_val = val
            arr[idx] = rank

        return arr