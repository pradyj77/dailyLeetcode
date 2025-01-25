from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        '''
        [
            [0,0,0,0,0,0,1,0],
            [0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,0,1,0,0,0,0,0]
        ]

        [
            [2,1,2,3,2,1,0,1],
            [1,0,1,2,3,2,1,2],
            [0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,0,1,0,0,1,0,1],
            [0,1,0,1,0,0,1,0]
        ]
        
        '''
        # height = []
        # for i in range(0, len(isWater)):
        #     height.append([-1] * len(isWater[0]))

        # for i in range(0, len(isWater)):
        #     for j in range(0, len(isWater[0])):
        #         if isWater[i][j] == 1:
        #             height[i][j] = 0
        
        # for i in range(0, len(height)):
        #     for j in range(0, len(height[i])):
        #         if height[i][j] == -1:
        #             rows = [-1, 1, 0, 0]
        #             cols = [0, 0, -1, 1]
        #             for k in range(0, 4):
        #                 newRow = i + rows[k]
        #                 newCol = j + cols[k]
        #                 if newRow >= 0 and newRow < len(height) and newCol >= 0 and newCol < len(height[0]):
        #                     if isWater[newRow][newCol] == 1: # This is water cell
        #                         height[i][j] = 1
                            
    
        # for i in range(0, len(height)):
        #     for j in range(0, len(height[0])):
        #         if height[i][j] == -1:
        #             height[i][j] = max(height[i][j], height[newRow][newCol] + 1)


        # return height

        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]  # Initialize heights to -1 to indicate unvisited cells
        queue = deque()
        
        # Initialize BFS with all water cells at height 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
        # BFS to assign heights to land cells
        while queue:
            x, y = queue.popleft()
            current_height = height[x][y]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = current_height + 1
                    queue.append((nx, ny))
        
        return height
