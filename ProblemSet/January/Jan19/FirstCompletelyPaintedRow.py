class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        '''
        [1,4,5,2,6,3]

        [4,3,5]
        [1,2,6]
        
        '''
        m = len(mat)
        n = len(mat[0])
        rowCount = 0
        colCount = 0
        locationMap = {}
        rowMap = {}
        colMap = {}

        for i in range(0, m):
            rowMap[i] = 0
        
        for i in range(0, n):
            colMap[i] = 0

        for i in range(0, m):
            for j in range(0, n):
                locationMap[mat[i][j]] = [i, j]

        # print("LOCATION MAP", locationMap)

        # print("ROW MAP", rowMap)
        # print("COL MAP", colMap)
        
        for i in range(0, len(arr)):
            #print("FOR ITEM", arr[i])
            row = locationMap[arr[i]][0]
            col = locationMap[arr[i]][1]

            rowMap[row] += 1
            colMap[col] += 1

            # print("ROW MAP", rowMap)
            # print("COL MAP", colMap)

            if rowMap[row] == n or colMap[col] == m:
                return i

        return -1

