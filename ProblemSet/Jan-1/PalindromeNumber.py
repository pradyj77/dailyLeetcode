class Solution:
    def isPalindrome(self, x: int) -> bool:

        # # Approach 1: Convert to a string
        # return str(x) == str(x)[::-1]

        if x < 0:
            return False

        if x == 0:
            return True

        ogNum = x
        reverseNum = ''
        while x > 0:
            #print(x)
            temp = x % 10
            #print(temp)
            x = x // 10
            reverseNum += str(temp)
        
        return ogNum == int(reverseNum)
