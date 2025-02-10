class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        9973

        9 - 9 - 7 - 3

        2736

        2 - 7 - 3 - 6

        4312

        4 - 3 - 2 - 1

        '''
        numArr = []
        for i in range(0, len(str(num))):
            numArr.append(str(num)[i])

        maxNum = int("".join(numArr))
        for i in range(0, len(numArr)):
            prev = numArr[i]
            tempMax = numArr[i]
            swapLocation = i
            for j in range(i + 1, len(numArr)):
                if numArr[j] > tempMax:
                    numArr[i], numArr[j] = numArr[j], numArr[i]
                    newNum = int("".join(numArr))
                    if newNum > maxNum:
                        maxNum = newNum
                    numArr[i], numArr[j] = numArr[j], numArr[i]
            
        return maxNum

