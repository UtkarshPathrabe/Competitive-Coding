class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrome(string, startIndex, endIndex):
            while endIndex - startIndex > 0:
                if string[startIndex] != string[endIndex]:
                    return False
                startIndex += 1
                endIndex -= 1
            return True
        
        def areTwoStringsPalindrome(string1, string2):
            startIndex, endIndex = 0, len(string1) - 1
            while endIndex - startIndex > 0 and string1[startIndex] == string2[endIndex]:
                startIndex += 1
                endIndex -= 1
            return isPalindrome(string1, startIndex, endIndex) or isPalindrome(string2, startIndex, endIndex)
        
        return areTwoStringsPalindrome(a, b) or areTwoStringsPalindrome(b, a)