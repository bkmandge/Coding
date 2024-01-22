"""
                    String Compression

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

"""


def compress(s):
    if len(s) <= 1:
        return s
    # count of current char
    # two pointers:- 1. count of char 2. to modify array in-place (updating char with count)
    i = 0
    j = 1

    count = 1  # storing j's count

    for j in range(1, len(s)):
        if s[j] != s[j - 1]:
            s[i] = s[j - 1]  # store prev char i.e. "a"
            if count >= 2:
                i += 1  # move current index to next to store count
                s[i] = str(count)
            i += 1  # move current index to next to check occurrences
            count = 1
        elif s[j] == s[j - 1]:
            count += 1

    s[i] = s[-1]
    if count >= 2:
        i += 1
        s[i] = str(count)

    return i + 1


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))