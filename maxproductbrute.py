array = [-3,0,1,-2] 


def maxProductBruteForce(array):
    # bruteForce = []

    maxProduct = float("-inf")
    currentProduct = 1


    for i in range(len(array)):
        currentProduct = array[i]
        maxProduct = max(maxProduct, currentProduct)

        for j in range(i+1, len(array)):
            currentProduct *= array[j]
            maxProduct = max(maxProduct, currentProduct)

    return maxProduct




print(maxProductBruteForce(array))


