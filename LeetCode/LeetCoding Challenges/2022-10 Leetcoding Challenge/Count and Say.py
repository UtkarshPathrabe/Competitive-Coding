class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        currentResult = self.countAndSay(n - 1)
        result, char, count = "", currentResult[0], 1
        for i in range(1, len(currentResult)):
            if currentResult[i] == char:
                count += 1
            else:
                result += str(count) + str(char)
                char, count = currentResult[i], 1
        return result + str(count) + str(char)