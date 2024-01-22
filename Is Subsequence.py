"""
                        Is Subsequence
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false

"""


def isSubsequence(s, t):
    # initialise i & j to starting index of each string
    i = j = 0

    while i < len(s) and j < len(t):
        # check if found matching char, if yes move both pointers
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            # else move only j pointer to check next char
            j += 1

    # as reached at the end of s string, check if found subsequence of not
    return True if i == len(s) else False


s = "axc"
t = "ahbgdc"

print(isSubsequence(s, t))
