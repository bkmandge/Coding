"""
                345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede"

"""


def reverse_vowels(s):
    # strings are immutable, so convert it into list
    s = list(s)

    # to check if string has any vowels in it
    vowels = set('aeiouAEIOU')

    left = 0
    right = len(s) - 1
    while left < right:
        # check left & right char in vowels, if yes swap them else move them
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)


s = "hello"
print(reverse_vowels(s))
