class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        '''
        [
            [1,0,0,1,0],
            [0,0,0,0,0],
            [0,0,0,1,0]
        ]
        
        '''

        # serverCount = 0
        # visited = {}

        # # Check row by row
        # for i in range(0, len(grid)):
        #     rowCount = 0
        #     for j in range(0, len(grid[0])):
        #         #print(tuple((i, j)))
        #         if grid[i][j] == 1:
        #             rowCount += 1
        #     if rowCount > 1:
        #         for j in range(0, len(grid[0])):
        #             if grid[i][j] == 1 and tuple((i, j)) not in visited:
        #                 #print("Found", tuple((i, j)))
        #                 visited[tuple((i, j))] = True

        # #print("after row count", serverCount)
        # # Check col by col
        # for i in range(0, len(grid[0])):
        #     colCount = 0
        #     for j in range(0, len(grid)):
        #         if grid[j][i] == 1:
        #             colCount += 1
        #     if colCount > 1:
        #         for j in range(0, len(grid)):
        #             if grid[j][i] == 1 and tuple((j, i)) not in visited:
        #                 #print("Found", tuple((j, i)))
        #                 visited[tuple((j, i))] = True

        # return len(visited)
        
        # Get grid dimensions
        m, n = len(grid), len(grid[0])
        
        # Count servers in each row and column
        rowCount = [0] * m
        colCount = [0] * n
        
        # First pass to calculate row and column server counts
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        
        # Second pass to count communicating servers
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rowCount[i] > 1 or colCount[j] > 1):
                    result += 1
        
        return result



