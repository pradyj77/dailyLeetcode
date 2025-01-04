class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        '''
            Count the freq of letters in the string
            All the possible combinations will be equal to number of chars with freq greater than equal to 2
            freqDict = {}
            indexDict = {}
            aabca
            a : 3 b : 1 c : 1
            a : [0,1,4], b : [2], c : [3]
            = 3

            adc
            a : 1, d : 1, c : 1
            a : [0], d : [1], c : [2]
            = 0

            bbcbaba | bbabcba
            b : 4, c : 1, a : 2
            b : [0, 5], c : [4], a : [2, 6]
            bcb, bbb, bab
            aba
            = 3

            if freq is 2:
                

        '''

        indexDict = {}
        palindromeCount = 0

        for i in range(0, len(s)):
            # if s[i] not in freqDict:
            #     freqDict[s[i]] = 1
            # else:
            #     freqDict[s[i]] += 1
            if s[i] not in indexDict:
                indexDict[s[i]] = [i, i]
            else:
                indexDict[s[i]] = [indexDict[s[i]][0], i]
        
        for key in indexDict:
            start = indexDict[key][0]
            end = indexDict[key][1]
            if end - start >= 2:
                # Palindrome is possible  
                palindromeCount += len(set(list(s[start+1:end])))
                    
        return palindromeCount

