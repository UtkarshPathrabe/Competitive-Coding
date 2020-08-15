class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        namePtr, typedPtr = 0, 0
        nameLength = len(name)
        typedLength = len(typed)
        while namePtr < nameLength and typedPtr < typedLength:
            if name[namePtr] == typed[typedPtr]:
                namePtr += 1
                typedPtr += 1
            elif typedPtr > 0 and typed[typedPtr] == typed[typedPtr - 1]:
                typedPtr += 1
            else:
                return False
        if namePtr != nameLength:
            return False
        else:
            while typedPtr < typedLength:
                if typed[typedPtr] != typed[typedPtr - 1]:
                    return False
                typedPtr += 1
        return True