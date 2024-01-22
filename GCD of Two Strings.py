"""
                    Greatest Common Divisor of Strings
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "LEET", str2 = "CODE"
Output: ""

"""


def gcdOfStrings(str1, str2) -> str:
    # check if both strings have any common prefix or not
    if str1 + str2 != str2 + str1:
        return ""

    # calculate gcd of both strings
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common_length = gcd(len(str1), len(str2))

    return str1[: common_length]



