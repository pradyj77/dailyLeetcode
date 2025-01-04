class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        # Example 1:

            01234567890123
            PAYPALISHIRING

            P   A   H   N
            A P L S I I G
            Y   I   R 

            PAHNAPLSIIGYIR

        # Example 2:

            01234567890123
            PAYPALISHIRING

            P     I     N
            A   L S   I G
            Y A   H R
            P     I

            PINALSIGYAHRPI

        # Example 3:

            01234567890123
            PAYPALISHIRING

            P       H  
            A     S I 
            Y   I   R
            P L     I G
            A       N

            PNASIYIRPLIGAN
        '''
        if numRows == 1 or numRows >= len(s):
            return s

        zigzagString = ""
        evenJump = numRows + numRows - 2
        oddJump = 0

        for i in range(0, numRows):
            start = i
            jumpTracker = 0
            prev = -1
            while start < len(s):
                if start != prev:
                    zigzagString += s[start]
                prev = start
                if jumpTracker % 2 == 0:
                    start += evenJump
                else:
                    start += oddJump
                jumpTracker += 1
            evenJump -= 2
            oddJump += 2

        return zigzagString
