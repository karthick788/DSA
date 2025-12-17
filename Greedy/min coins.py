class Solution:
    def findMin(self, n):
        coin = 10           
        cnt = 0
        
        while n > 0:
            cnt += (n // coin)
            n = n % coin
            coin = coin // 2
            
        return cnt