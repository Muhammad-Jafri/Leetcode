class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        adj_list = {}
        for i in range(len(graph)):
            adj_list[i] = graph[i]

        
        