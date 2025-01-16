class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            currentWord = word
            for newWord in words:
                if newWord != currentWord and word in newWord:
                    result.append(word)
                    break
            
        return result