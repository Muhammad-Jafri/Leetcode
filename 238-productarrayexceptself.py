array = [1,2,3,4]


def productExceptSelf(array):
    productList = []


    for i in range(len(array)):

        product = 1

        for j in range(0, i):
            product *= array[j]

        for k in range(i+1, len(array)):
            product *= array[k]

        productList.append(product)


    return productList



print(productExceptSelf(array))



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        productList = []

        for i in range(len(nums)):

            product = 1

            for j in range(0, i):
                product *= nums[j]

            for k in range(i+1, len(nums)):
                product *= nums[k]

            productList.append(product)


        return productList
            
        