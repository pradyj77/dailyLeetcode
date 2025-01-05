class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        '''
        "abc"
        [[0,1,0],[1,2,1],[0,2,1]]

        [0,0,0]
        [-1,0,1]
        [-1,1,1]
        [0,1,1]

        [0,1,2]

        [0, 1, 0]

        ace
        
        '''


        alphabetDict = {'a':['z','b'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['c', 'e'], 'e': ['d', 'f'], 'f': ['e', 'g'], 'g': ['f','h'], 'h': ['g', 'i'], 'i': ['h', 'j'], 'j': ['i','k'], 'k': ['j','l'], 'l': ['k','m'], 'm': ['l','n'], 'n': ['m','o'], 'o': ['n','p'], 'p': ['o','q'], 'q': ['p','r'], 'r': ['q','s'], 's': ['r','t'], 't': ['s','u'], 'u': ['t','v'], 'v': ['u','w'], 'w': ['v','x'], 'x': ['w','y'], 'y': ['x','z'], 'z':['y','a']}
        strList = [0 for i in s]
        
        for shift in shifts:
            start = shift[0]
            end = shift[1]
            #print(strList)
            # if shift[2] == 1:
            #     for i in range(start, end + 1):
            #         if 0 <= i and i < len(s):
            #             strList[i] = alphabetDict[strList[i]][1]
            # else:
            #     for i in range(start, end + 1):
            #         if 0 <= i and i < len(s):
            #             strList[i] = alphabetDict[strList[i]][0]
            #print(strList)
            if shift[2] == 1:
                # for i in range(start, end + 1):
                #     if 0 <= i and i < len(s):
                #         strList[i] += 1
                strList[start] += 1
                if end + 1 < len(s):
                    strList[end + 1] -= 1
            else:
                # for i in range(start, end + 1):
                #     if 0 <= i and i < len(s):
                #         strList[i] -= 1
                strList[start] -= 1
                if end + 1 < len(s):
                    strList[end + 1] += 1
            
            
        for i in range(1, len(s)):
                strList[i] += strList[i - 1]

        #print(strList)
        result = ""
        # for i in range(0, len(strList)):
        #     temp = s[i]
        #     if strList[i] > 0:
        #         for j in range(0, strList[i]):
        #             temp = alphabetDict[temp][1]
        #     elif strList[i] < 0:
        #         for j in range(strList[i], 0):
        #             temp = alphabetDict[temp][0]
        #     result += temp

        for i in range(0, len(strList)):
            shift = strList[i]
            newChar = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result += newChar

        #return "".join(strList)
        return result
