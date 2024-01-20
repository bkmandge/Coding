"""
                            Find Words Containing Character
Input: words = ["leet","code"], x = "e"
Output: [0,1]

Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

"""

from typing import *
def findWordsContaining(words: List[str], x: str) -> List[int]:
    idx = []
    for i in range(len(words)):
        if x in words[i]:
            idx.append(i)
    return idx


words = ["leet","code"]
x = 'e'

print(findWordsContaining(words, x))