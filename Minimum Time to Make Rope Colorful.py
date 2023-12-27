class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        out = 0
        for i in range(len(colors) - 2, -1, -1):
            if colors[i + 1] == colors[i]:
                if (neededTime[i] > neededTime[i + 1]):
                    out += neededTime[i + 1]
                    neededTime[i + 1] = neededTime[i]
                else:
                    out += neededTime[i]
                    neededTime[i] = neededTime[i + 1]
        return out
