class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        

        dp = [0 for i in range(len(cost) + 1)]


        for i in range(len(cost) - 1, -1, -1):
            if(i == len(cost) - 1):
                dp[i] = cost[i]
            else:
                
                dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        
        return min(dp[0], dp[1])
    



array = [10,15,20]

sol = Solution()

print(sol.minCostClimbingStairs(array))


        