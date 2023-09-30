class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


        #case 1 player 1 starts from the first position 

        dp = [(0,0) for i in range(len(nums))]
        dp[0] = (nums[0],0)

        for i in range(1,len(nums)):
            j = len(nums) - i - 1

            if (i % 2 != 0): #player 2 turn 
                dp[i][1] = nums[i]
                dp[i][1] = nums[j]


        

        