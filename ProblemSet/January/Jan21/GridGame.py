from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        '''
        
        Robots can only move to right OR down
        Robot 1 wants to minimize points earned by Robot 2 aka traverse path with max points
        Robot 2 wants to maximize its points

        New problem: Find optimal path for robot 1 
                        -> convert all points on robot1's optimal path to be 0s
                            -> Find optimal path for robot 2 on new grid
        
        How to find optimal path?
        
        At every step we can make one of two choices leading to optimum path - DP

        every cell's value = max(currentValue + grid[r - 1][c], currentValue + grid[r][c - 1])
         
        
        '''

        # dpArray = {}
        # for i in range(0, len(grid)):
        #     for j in range(0, len(grid[0])):
        #         currentTuple = tuple((i,j))
        #         dpArray[currentTuple] = [0, [tuple((0,0))]]
    
        # #print(dpArray)

        # for i in range(0, len(grid)):
        #     for j in range(0, len(grid[0])):
        #         #print("DP ARRAY", dpArray)
        #         curr = tuple((i,j))
        #         if i == 0 and j == 0:
        #             dpArray[curr] = [grid[i][j], [tuple((i,j))]]
        #         elif i == 0:
        #             dpArray[curr][0] = dpArray[tuple((i,j - 1))][0] + grid[i][j]
        #             dpArray[curr][1] = dpArray[tuple((i,j - 1))][1] + [tuple((i,j))]
        #         elif j == 0:
        #             dpArray[curr][0] = dpArray[tuple((i - 1,j))][0] + grid[i][j]
        #             dpArray[curr][1] = dpArray[tuple((i - 1,j))][1] + [tuple((i,j))]
        #         else:
        #             dpArray[curr][0] = max(dpArray[tuple((i - 1,j))][0], dpArray[tuple((i,j - 1))][0]) + grid[i][j]
        #             if dpArray[tuple((i - 1,j))][0] >= dpArray[tuple((i,j - 1))][0]:
        #                 dpArray[tuple((i,j))][1] = dpArray[tuple((i - 1,j))][1] + [tuple((i, j))]
        #             else:
        #                 dpArray[tuple((i,j))][1] = dpArray[tuple((i,j - 1))][1] + [tuple((i, j))]

        # optimalPath = dpArray[tuple((len(grid) - 1, len(grid[0]) - 1))][1]
        # #print(optimalPath)

        # for item in optimalPath:
        #     grid[item[0]][item[1]] = 0

        # #print(grid)

        # newDpArray = []

        # for i in range(0, len(grid)):
        #     newDpArray.append([0] * len(grid[0]))

        # #print(newDpArray)

        # for i in range(0, len(grid)):
        #     for j in range(0, len(grid[0])):
        #         #print("DP ARRAY", dpArray)
        #         if i == 0 and j == 0:
        #             newDpArray[i][j] = grid[i][j]
        #         elif i == 0:
        #             newDpArray[i][j] = newDpArray[i][j - 1] + grid[i][j]
        #         elif j == 0:
        #             newDpArray[i][j] = newDpArray[i - 1][j] + grid[i][j]
        #         else:
        #             newDpArray[i][j] = max(newDpArray[i - 1][j], newDpArray[i][j - 1]) + grid[i][j]

        # return newDpArray[-1][-1]

        n = len(grid[0])
        
        # Compute prefix sums for both rows
        topSum = [0] * n
        bottomSum = [0] * n
        
        topSum[0] = grid[0][0]
        bottomSum[0] = grid[1][0]
        
        for i in range(1, n):
            topSum[i] = topSum[i - 1] + grid[0][i]
            bottomSum[i] = bottomSum[i - 1] + grid[1][i]
        
        totalTop = topSum[-1]  # Sum of all points in row 0
        totalBottom = bottomSum[-1]  # Sum of all points in row 1
        
        # Iterate over possible split points
        minPointsForSecondRobot = float('inf')
        
        for j in range(n):
            pointsAbove = totalTop - topSum[j]  # Remaining points in top row after column j
            pointsBelow = bottomSum[j - 1] if j > 0 else 0  # Points in bottom row before column j
            maxPointsSecondRobot = max(pointsAbove, pointsBelow)
            
            minPointsForSecondRobot = min(minPointsForSecondRobot, maxPointsSecondRobot)
        
        return minPointsForSecondRobot
        