class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        '''
        1231
        - 231
        - 123

        141231
        - 41231
        - 14123
        - 14231

        535653
        - 6513
        - 5613

        7673
        - 673
        - 763

        88981
        - 8981
        - 8891

        535653
        - 35653
        - 53653
        - 53563

        '''
        breakPoint = ""
        lastCheckpoint = len(number) - 1

        for i in range(0, len(number)):
            if number[i] == digit:
                lastCheckpoint = i
                if i < len(number) - 1 and number[i] < number[i + 1]:
                    breakPoint = i
                    break
        
        if breakPoint == "":
            return number[:lastCheckpoint] + number[lastCheckpoint+1:]

        return number[:breakPoint] + number[breakPoint+1:]