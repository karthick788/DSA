class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        h = []
        ans = Counter(hand)
        for key in ans:
            heapq.heappush(h,key)

        while h:
            start = h[0]
            for card in range(start,start+groupSize):
                if card not in ans:
                    return False
                ans[card] -= 1

                if ans[card] == 0:
                    if card != h[0]:
                        return False

                    heapq.heappop(h)
                    del ans[card]

        return True