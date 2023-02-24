class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        frequencyMap = defaultdict(int)
        bulls = cows = 0
        for index, s in enumerate(secret):
            g = guess[index]
            if s == g:
                bulls += 1
            else:
                cows += int(frequencyMap[s] < 0) + int(frequencyMap[g] > 0)
                frequencyMap[s] += 1
                frequencyMap[g] -= 1
        return '{}A{}B'.format(bulls, cows)