class Solution:
    def allPathsSourceTarget(self, graph):
        end = len(graph) - 1

        def dfs(node, path, output):
            
            if node == end:
                output.append(path)
            
            for nx in graph[node]:
                dfs(nx, path + [nx], output)
        
        output = []
        dfs(0,[0], output)

        return output
    
    

graph = [[4,3,1],[3,2,4],[3],[4],[]]
sol = Solution()
print(sol.allPathsSourceTarget(graph))