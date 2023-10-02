array = [2,5,3,4,1]


def countDP(array):

    count = 0

    for i in range(len(array)):

        left_greater, left_smaller, right_greater, right_smaller = 0,0,0,0
        
        for j in range(0, i): #checking for nums less than i in case of ascending and greater than i in case of descending

            if(array[j] < array[i]):
                left_smaller+=1
            if(array[j] > array[i]):
                left_greater+=1
            

        for k in range(i+1, len(array)): #checking for nums greater than i in case of ascending and less than i in case of descending
            if(array[k] < array[i]):
                right_smaller+=1
            if(array[k] > array[i]):
                right_greater+=1

        count+=left_smaller * right_greater + left_greater * right_smaller
    
    return count


print(countDP(array))




class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        count = 0

        for i in range(len(rating)):

            left_greater, left_smaller, right_greater, right_smaller = 0,0,0,0
            
            for j in range(0, i): #checking for nums less than i in case of ascending and greater than i in case of descending

                if(rating[j] < rating[i]):
                    left_smaller+=1
                if(rating[j] > rating[i]):
                    left_greater+=1
                

            for k in range(i+1, len(rating)): #checking for nums greater than i in case of ascending and less than i in case of descending
                if(rating[k] < rating[i]):
                    right_smaller+=1
                if(rating[k] > rating[i]):
                    right_greater+=1

            count+=left_smaller * right_greater + left_greater * right_smaller
        
        return count






    


