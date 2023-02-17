class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE_CODE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len({''.join(MORSE_CODE[ord(char) - ord('a')] for char in word) for word in words})