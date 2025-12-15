class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        value = Counter(tasks)
        val = list(value.values())
        h = []

        for i in val:
            heapq.heappush(h,-i)
        
        time = 0
        cycles = n+1

        while h:
            i = 0
            temp = []
            while i < cycles and h:
                freq = -heapq.heappop(h)
                freq -= 1
                time += 1
                if freq > 0:
                    temp.append(freq)
                i += 1

            for k in temp:
                heapq.heappush(h,-k)

            if h:
                time += (cycles - i)

        return time