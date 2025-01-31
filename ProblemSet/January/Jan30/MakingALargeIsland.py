# # Take 1:

# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         '''
#         1 0 0 1
#         1 1 0 1
#         1 0 0 1
#         1 1 1 0
        
#         '''
#         islandSize = {}
#         islandGroupMap = {}
#         def getIslandSize(position, islandGroup):

#             # print("NEWCALL")
#             # print()

#             myStack = [[position[0], position[1]]]
#             visited = {}
#             size = 0
#             while myStack:
#                 # print()
#                 # print("HEHE", myStack)
#                 # print()
#                 curr = myStack.pop(0)
#                 size += 1
#                 x = curr[0]
#                 y = curr[1]
#                 visited[tuple((x,y))] = True
#                 rows = [-1, 1, 0, 0]
#                 cols = [0, 0, -1, 1]
#                 #print("WHATS VISITED", visited)

#                 for i in range(0, 4):
#                     newRow = x + rows[i]
#                     newCol = y + cols[i]

#                     if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]):
#                         #print("Printing grid values", grid[newRow][newCol])
#                         if tuple((newRow, newCol)) not in visited and grid[newRow][newCol] == 1:
#                             #print("REACHED HERE", tuple((newRow, newCol)))
#                             myStack.append([newRow, newCol])

#             #print("FINAL SIZE IS", size)
#             for item in visited:
#                 islandSize[item] = size
#                 islandGroupMap[item] = islandGroup
#             #print("AFTER FINAL", islandSize)
#             return

#         islandCounter = 0
#         for i in range(0, len(grid)):
#             for j in range(0, len(grid[i])):
#                 if grid[i][j] == 1 and tuple((i, j)) not in islandSize:
#                     islandCounter += 1
#                     getIslandSize([i, j], islandCounter)

#         print(islandSize)
#         print(islandGroupMap)

#         grandMax = float("-inf")

#         # Now loop through each island component and check for neighbors + 1 and get max score

#         def findNeighbourIsland(position):
#             print("SHOWING NOW", position)
#             x = position[0]
#             y = position[1]
#             rows = [-2, 2, 0, 0]
#             cols = [0, 0, -2, 2]
#             #print("WHATS VISITED", visited)
#             for i in range(0, 4):
#                 newRow = x + rows[i]
#                 newCol = y + cols[i]
                
#                 if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]):
#                     print("POTENTIAL LOCATION 1 --", newRow, newCol)
#                     #print("Printing grid values", grid[newRow][newCol])
#                     if grid[newRow-1][newCol-1] == 0 and grid[newRow][newCol] == 1 and islandGroupMap[tuple((newRow,newCol))] != islandGroupMap[tuple((newRow,newCol))]:
#                         print("POTENTIAL LOCATION", newRow, newCol)
#                         #print("REACHED HERE", tuple((newRow, newCol)))
#                         grandMax = max(grandMax, islandSize[tuple((newRow,newCol))] + islandSize[tuple((newRow,newCol))])

#         for i in range(0, len(grid)):
#             for j in range(0, len(grid[i])):
#                 if grid[i][j] == 1:
#                     findNeighbourIsland([i, j])

#         return grandMax
        

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_sizes = {}
        island_id = 2

        # Step 1: Mark all islands and calculate their sizes
        for current_row in range(len(grid)):
            for current_column in range(len(grid[0])):
                if grid[current_row][current_column] == 1:
                    island_sizes[island_id] = self.explore_island(
                        grid, island_id, current_row, current_column
                    )
                    island_id += 1

        # If there are no islands, return 1
        if not island_sizes:
            return 1

        # If the entire grid is one island, return its size or size +
        if len(island_sizes) == 1:
            island_id -= 1
            return (
                island_sizes[island_id]
                if island_sizes[island_id] == len(grid) * len(grid[0])
                else island_sizes[island_id] + 1
            )

        max_island_size = 1

        # Step 2: Try converting every 0 to 1 and calculate the resulting island size
        for current_row in range(len(grid)):
            for current_column in range(len(grid[0])):
                if grid[current_row][current_column] == 0:
                    current_island_size = 1
                    neighboring_islands = set()

                    # Check down
                    if (
                        current_row + 1 < len(grid)
                        and grid[current_row + 1][current_column] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row + 1][current_column]
                        )

                    # Check up
                    if (
                        current_row - 1 >= 0
                        and grid[current_row - 1][current_column] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row - 1][current_column]
                        )

                    # Check right
                    if (
                        current_column + 1 < len(grid[0])
                        and grid[current_row][current_column + 1] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row][current_column + 1]
                        )

                    # Check left
                    if (
                        current_column - 1 >= 0
                        and grid[current_row][current_column - 1] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row][current_column - 1]
                        )

                    # Sum the sizes of all unique neighboring islands
                    for island_id in neighboring_islands:
                        current_island_size += island_sizes[island_id]
                    max_island_size = max(max_island_size, current_island_size)

        return max_island_size

    def explore_island(
        self,
        grid: List[List[int]],
        island_id: int,
        current_row: int,
        current_column: int,
    ) -> int:
        if (
            current_row < 0
            or current_row >= len(grid)
            or current_column < 0
            or current_column >= len(grid[0])
            or grid[current_row][current_column] != 1
        ):
            return 0

        grid[current_row][current_column] = island_id

        return (
            1
            + self.explore_island(
                grid, island_id, current_row + 1, current_column
            )
            + self.explore_island(
                grid, island_id, current_row - 1, current_column
            )
            + self.explore_island(
                grid, island_id, current_row, current_column + 1
            )
            + self.explore_island(
                grid, island_id, current_row, current_column - 1
            )
        )