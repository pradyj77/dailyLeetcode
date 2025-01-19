class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq

        if not heightMap or not heightMap[0]:
            return 0
    
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Add all boundary cells into the min-heap
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = visited[i][n - 1] = True
        
        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = visited[m - 1][j] = True
        
        trapped_water = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Process the heap
        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Calculate water trapped
                    trapped_water += max(0, height - heightMap[nx][ny])
                    # Update height boundary and add neighbor to the heap
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        
        return trapped_water 