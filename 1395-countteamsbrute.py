array = [1,2,3,4]

def countTeams(array):
    combinations = []

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                if((array[i] < array[j] and array[j] < array[k]) or (array[i] > array[j] and array[j] > array[k])):
                    combinations.append([array[i],array[j],array[k]])

    return len(combinations)



print(countTeams(array))

class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        combinations = []
        count = 0

        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                for k in range(j+1, len(rating)):
                    if((rating[i] < rating[j] and rating[j] < rating[k]) or (rating[i] > rating[j] and rating[j] > rating[k])):
                        # combinations.append([rating[i],rating[j],rating[k]])
                        count+=1

        return count

        
            
