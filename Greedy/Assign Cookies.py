class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i,j = 0,0
        n1,n2 = len(g),len(s)

        while i < n1 and j < n2:
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i

