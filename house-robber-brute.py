




def maxProfit(array, index, total): #wtf i wrote it and i don't know how it works
    if(index >= total):
        return 0
    if(array[index] == array[total - 1]):
        return array[index]

    c = max(maxProfit(array,index+2,total), maxProfit(array,index+3,total))

    return array[index] + c



array = [2,7,9,3,1]
total = 5

print(maxProfit(array,0,total))