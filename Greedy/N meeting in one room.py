class Solution:
    def maximumMeetings(self,start,end):
        timings = []
        for i,j in zip(start,end):
            timings.append([i,j])
            
        timings.sort(key = lambda x:x[1])
        freetime = -1
        cnt = 0
        for i in range(len(timings)):
            if freetime < timings[i][0]:
                cnt += 1
                freetime = timings[i][1]
                
        return cnt