#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    characterFrequency = Counter(s)
    print(characterFrequency)
    frequencyOfCharacterFrequency = Counter(characterFrequency.values())
    print(frequencyOfCharacterFrequency)
    if len(frequencyOfCharacterFrequency) == 1 or len(frequencyOfCharacterFrequency) == 0:
        return 'YES'
    elif len(frequencyOfCharacterFrequency) > 2:
        return 'NO'
    else:
        if 1 in frequencyOfCharacterFrequency.values():
            if frequencyOfCharacterFrequency[min(frequencyOfCharacterFrequency.keys())] == 1 or (max(frequencyOfCharacterFrequency.keys()) - min(frequencyOfCharacterFrequency.keys()) == 1):
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
