class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [0 for i in range(len(nums) + 1)]

        for i in range(len(nums) - 1, -1, -1):
            if (i == len(nums) - 1):
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + max(dp[i+2:])



        return max(dp[0],dp[1])
    


sol = Solution()

nums = [2,7,9,3,1]

print(sol.rob(nums))