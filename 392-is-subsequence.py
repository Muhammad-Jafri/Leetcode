
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

s = ""
t = "ahbgdc"


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(s == ""):
            if(t== "" or len(t)>=1):
                return True
        

        ssubsequenceoft = False

        startingPoint = 0
        count = 0

        indexS = 0
        for i in range(startingPoint, len(t)):
            charS = s[indexS]

            if(charS == t[i]):
                count+=1
                indexS+=1
                startingPoint = i
        
        return (count == len(s))
    

sol = Solution()
print(sol.isSubsequence(s,t))







