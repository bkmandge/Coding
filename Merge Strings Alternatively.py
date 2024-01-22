"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

"""


def merge_strings_alternatively(word1, word2):
    index1 = 0
    index2 = 0

    res = []

    while index1 < len(word1) and index2 < len(word2):
        res.append(word1[index1])
        res.append(word2[index2])

        index1 += 1
        index2 += 1

    res.append(word1[index1:])
    res.append(word2[index2:])

    return "".join(res)


word1 = "ab"
word2 = "pqrs"

print(merge_strings_alternatively(word1, word2))
