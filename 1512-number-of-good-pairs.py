# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]==nums[j]):
                    count+=1

        return count
        


sol = Solution()
array = [1,1,1,1]

print(sol.numIdenticalPairs(array))