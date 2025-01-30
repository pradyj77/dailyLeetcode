class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxFish = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                #print(":NEW", i, j)
                if grid[i][j] != 0:
                    visited = {}
                    stack = [(i, j)]
                    visited[tuple((i,j))] = True
                    currentFishCount = 0
                    while stack:
                        #print(stack)
                        #print("Current count", currentFishCount)
                        curr = stack.pop(0)
                        currRow = curr[0]
                        currCol = curr[1]
                        currCount = grid[currRow][currCol]
                        #print("HERE", currCount)
                        currentFishCount += currCount
                        if currCount != 0:
                            rows = [0, 0, 1, -1]
                            cols = [1, -1, 0, 0]
                            
                            for k in range(0, 4):
                                newRow = currRow + rows[k]
                                newCol = currCol + cols[k]
                                if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]) and grid[newRow][newCol] != 0 and tuple((newRow, newCol)) not in visited:
                                    visited[tuple((newRow, newCol))] = True
                                    stack.append((newRow, newCol))
                                    #print("STACK UPDATED?? - yes")


                    maxFish = max(maxFish, currentFishCount)
        
        return maxFish
