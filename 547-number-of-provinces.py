# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

def compareArrays(first,second): #return true if second array contains element as the first array too, 
    smallArray = []
    bigArray = []
    if(len(first) <= len(second)):
        smallArray = first
        bigArray = second
    else:
        smallArray = second
        bigArray = first
    
    flag = True #we are assuming that first array has some elements that are present in second as well
    for i in range(len(smallArray)):
        if(smallArray[i] not in bigArray):
            flag = False
            break
    
    return flag



def bfs(startingNode,adjacencyMatrix):
    
    visited = []
    stackStruct = []
    stackStruct.append(startingNode)

    while(stackStruct):
        currentNode = stackStruct.pop(0)
        if(currentNode in visited):
            continue
        visited.append(currentNode)
        for i in range(len(adjacencyMatrix[currentNode])):
            if(adjacencyMatrix[currentNode][i] == 1):
                stackStruct.append(i)
    
    return visited






class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        numOfProvince = 1
        visited = bfs(0, isConnected)

        for i in range(1,len(isConnected)):
            bfsCurNode = bfs(i,isConnected)
            if not (compareArrays(visited, bfsCurNode)):
                numOfProvince += 1

            for i in bfsCurNode:
                visited.append(i)

        return numOfProvince

            
        



        

        


adjacencyList = [[1,0,0],[0,1,0],[0,0,1]]

# print(bfs(2,adjacencyList))

sol = Solution()
print(sol.findCircleNum(adjacencyList))

# print(compareArrays([1,23], [1,2,1,2]))