.# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         '''
#         - Check all the terminal nodes
#         - Find all safe nodes directly going into terminal nodes
#         - 
        
#         [[1,2],[2,3],[5],[0],[5],[],[]]

#         terminal nodes = 5, 6

#         safe nodes to terminal nodes = 2, 4

#         nodes going into safe nodes => 

#         0 -> 1, 2, 3, 4
#         1 -> 1, 2
#         2 -> 3, 4
#         3 -> 0, 4
#         4 -> []

#         [[],[0,2,3,4],[3],[4],[]]

#         0 -> []
#         1 -> 0, 2, 3, 4
#         2 -> 3
#         3 -> 4
#         4 -> []

#         [1] {}
#         [0, 2, 3, 4] {1}
#         [2, 3, 4] {1,0}
#         [3, 4, 3] {1,0,2}
#         [4, 3, 4] {1,0,2,3}
#         [3,4]   {1,0,2,3,4}
#         '''
#         # terminal_nodes = {}

#         # for i in range(0, len(graph)):
#         #     if len(graph[i]) == 0:
#         #         terminal_nodes[i] = True
        
#         # #print(terminal_nodes)

#         # for i in range(0, len(graph)):
#         #     isSafe = True
#         #     for j in range(0, len(graph[i])):
#         #         if graph[i][j] not in terminal_nodes:
#         #             isSafe = False
#         #     if isSafe:
#         #         terminal_nodes[i] = True
        
#         # #print(terminal_nodes)

#         # result = []

#         # for key in terminal_nodes:
#         #     result.append(key)
        
#         # result.sort()

#         # def isSafe(node, visited):
#         #     print("CALLED", node)
#         #     if node in visited:
#         #         return
#         #     visited[node] = True
#         #     if len(graph[node]) == 0:
#         #         return True
#         #     else:
#         #         isSafeFlag = True
#         #         for i in range(0, len(graph[node])):
#         #             curr = graph[node][i]
#         #             if curr != node:
#         #                 isSafeFlag = isSafeFlag and isSafe(curr, visited)
#         #             else:
#         #                 continue
                
#         #         return isSafeFlag

#         def isSafe(node):
            
#             print("NODE", node)
#             visited = {node: True}
#             stack = [node]
#             cycleFound = False

#             while stack:
#                 print("MY STACK", stack)
#                 top = stack.pop(0)
#                 print("VISITED", visited)
#                 visited[top] = True
#                 adjacentNodes = graph[top]
#                 for i in range(0, len(adjacentNodes)):
#                     if adjacentNodes[i] in visited:
#                         cycleFound = True
#                         break
#                     elif adjacentNodes[i] not in stack:
#                         stack.append(adjacentNodes[i])
                        
#                 if cycleFound:
#                     break

#             return not cycleFound

#         result = []

#         for i in range(0, len(graph)):
#             if isSafe(i):
#                 result.append(i)

#         return result
# \
        
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # State: 0 = not visited, 1 = visiting, 2 = safe
        n = len(graph)
        state = [0] * n
        
        def dfs(node):
            if state[node] != 0:  # Already visited
                return state[node] == 2  # Return True if already marked safe
            
            state[node] = 1  # Mark as visiting
            for neighbor in graph[node]:
                if state[neighbor] == 1 or not dfs(neighbor):  # Cycle detected
                    return False
            
            state[node] = 2  # Mark as safe
            return True
        
        # Perform DFS for all nodes
        result = []
        for i in range(n):
            if dfs(i):
                result.append(i)
        
        return result
