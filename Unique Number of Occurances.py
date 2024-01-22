"""
                            Unique Number of Occurances

Return True if two values do not have the same number of occurrences.

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Input: arr = [1,2]
Output: false
Explanation: 1 -> occcured 1 time, 2 -> also occured 1 time so False

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""


def uniqueOccurances(arr):
    # create dict1 to store key and values count
    dict1 = {}
    for i in arr:
        dict1[i] = dict1.get(i, 0) + 1

    # create hashset of values from dict1
    set1 = set(dict1.values())
    # print(dict1.items())
    # print(set1)

    # check if length of set and dict1 values are same or not
    return len(set1) == len(dict1.values())


arr = [1,2]
print(uniqueOccurances(arr))