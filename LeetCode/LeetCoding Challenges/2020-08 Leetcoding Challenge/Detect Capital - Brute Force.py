class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) > 2:
            firstCharacterCapital = word[0].isupper()
            secondCharacterCapital = word[1].isupper()
            for i in range(2, len(word)):
                if word[i].isupper() and firstCharacterCapital and secondCharacterCapital:
                    continue
                elif not secondCharacterCapital and word[i].islower():
                    continue
                else:
                    return False
            return True
        elif len(word) == 2:
            if word[0].islower() and word[1].isupper():
                return False
            else:
                return True
        else:
            return True