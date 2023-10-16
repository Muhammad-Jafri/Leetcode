# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.



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
        citiesOfArbitrary = len(bfs(0,isConnected))

        for i in range(1, len(isConnected)):
            citiesPrime = len(bfs(i, isConnected))

            if(citiesPrime == 1):
                numOfProvince+=1
                continue

            if(citiesOfArbitrary != citiesPrime):
                numOfProvince+=1
                temp = citiesOfArbitrary
                citiesOfArbitrary = citiesPrime
                citiesPrime = temp
        
        return numOfProvince


adjacencyList = [[1,1,0],[1,1,0],[0,0,1]]

print(bfs(2,adjacencyList))

sol = Solution()
print(sol.findCircleNum(adjacencyList))

