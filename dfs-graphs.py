#function to perform dfs from source node

def dfs(source, adjacency_list, vertices = []):

    vertices = [False for i in range(len(adjacency_list))]
    
    def dfs_helper(source):

        if vertices[source]:
            return 
        vertices[source] = True

        nbhd = adjacency_list[source]
        for nxt in nbhd:
            dfs(nbhd)

        return vertices
    
    dfs_helper(vertices)

    



graphDict = {0:[1,3,4],
            1:[4,3,2],
            2:[3],
            3:[4],
            4:[]
            }


source_node = 0

print(dfs(source_node, graphDict))