class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        '''
        [[1,4],[2,5],[1,3],[3,4]]
        ball 7 -> color 4 ==> 1  | 4 : [7]
        ball 1 -> color 4 ==> 1  | 4 : [7, 1]
        ball 2 -> color 5 ==> 2  | 5 : [2], 4: [7, 1]
        ball 1 -> color 5 ==> 2  | 5 : [2, 1], 4: [7] 
        ball 1 -> color 3 ==> 3  | 3 : [1], 5 : [2], 4 : [7]
        ball 3 -> color 4 ==> 3  | 3 : [1], 5 : [2], 4 : [7, 3]


        - While iterating
            - Check if color is already visited:
                - if yes:
                    - Check if ball is already visited:
                        - if yes:
                            - Remove ball's current color's count
                            - Color count will decrease
                        - if no:
                            - Add to color's list
                - if no:
                    - if ball is already visited:
                        - if yes:
                            - Remove ball from it's current color
                        Add ball to new color      
        
        '''

        colorMap = {}
        #colors = [0 for i in range(limit+1)]
        #print(colors)
        ballColor = {}
        result = []
        
        for index, mapping in enumerate(queries):

            ball = mapping[0]
            color = mapping[1]

            # print("colors", colors)
            # print()
            # print("map", colorMap)
            # print()
            if color in colorMap:
                # Check if this ball was already counted
                if ball in ballColor and ballColor[ball] != color:
                    # Find out what color was already assigned
                    prevColor = ballColor[ball]
                    colorMap[prevColor] -= 1
                    if colorMap[prevColor] == 0:
                        del colorMap[prevColor]
                if ball in ballColor:
                    if ballColor[ball] != color:
                        colorMap[color] += 1
                else:
                    colorMap[color] += 1
            else:
                if ball in ballColor:
                    prevColor = ballColor[ball]
                    colorMap[prevColor] -= 1
                    if colorMap[prevColor] == 0:
                        del colorMap[prevColor]
                colorMap[color] = 1
            ballColor[ball] = color

            result.append(len(colorMap))

        return result
