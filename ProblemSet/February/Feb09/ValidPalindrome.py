import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # s = s.replace(' ','')
        # s = s.strip()
        '''
        abcba
        mid = 5 // 2 = 2
        
        012345
        abccba
        mid = 6 // 2 = 3
        '''
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]+', '', s)
        mid = len(s) // 2
        stack = []
        print(s)
        for i in range(0, mid):
            stack.append(s[i])

        if len(s) % 2 != 0:
            mid = mid + 1
        
        for i in range(mid, len(s)):
            curr = stack.pop()
            if s[i] != curr:
                return False

        return True

        