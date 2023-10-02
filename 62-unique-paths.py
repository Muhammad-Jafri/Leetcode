#m x n grid
#robot can only move either down or right
#starts at (0,0) and need to reach to the end of the grid i.e (m-1,n-1)
#the output should be the number of unique paths that the robot can take


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        rows = m
        cols = n

        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m-1, -1 , -1):
            
            for j in range(n-1,-1,-1):

                if(i == rows - 1 or j == cols - 1):
                    dp[i][j] = 1

                else:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j]
        
        return dp[0][0]


                




sol = Solution()
print(sol.uniquePaths(3,7))


        
        