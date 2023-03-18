class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Number of bytes in the current UTF-8 character
        currentCharacterLength = 0
        # Mask to check if the most significant bit (8th bit from the left) is set or not
        mask1 = 1 << 7
        # Mask to check if the second most significant bit is set or not
        mask2 = 1 << 6
        for number in data:
            # Get the number of set most significant bits in the byte if
            # this is the starting byte of an UTF-8 character.
            mask = 1 << 7
            if currentCharacterLength == 0:
                while mask & number:
                    currentCharacterLength += 1
                    mask = mask >> 1
                # 1 byte characters
                if currentCharacterLength == 0:
                    continue
                # Invalid scenarios according to the rules of the problem
                if currentCharacterLength == 1 or currentCharacterLength > 4:
                    return False
            else:
                # If this byte is a part of an existing UTF-8 character, then we
                # simply have to look at the two most significant bits and we make
                # use of the masks we defined before.
                if not ((number & mask1) and not (number & mask2)):
                    return False
            currentCharacterLength -= 1
        return currentCharacterLength == 0