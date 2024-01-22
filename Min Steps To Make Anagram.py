"""
                    Min Steps To Make Anagram

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

"""


def minSteps(self, s: str, t: str) -> int:
    if len(s) != len(t):
        return -1

    count_S = [0] * 26
    count_T = [0] * 26

    for char in s:
        count_S[ord(char) - ord('a')] += 1

    for char in t:
        count_T[ord(char) - ord('a')] += 1

    return sum(abs(count_S[i] - count_T[i]) for i in range(26)) // 2