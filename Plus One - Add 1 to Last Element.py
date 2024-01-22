"""
                        Plus One
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

"""


def plusOne(digits):
    idx = len(digits) - 1

    while idx >= 0:
        if digits[idx] == 9:
            digits[idx] = 0
        else:
            # here adding carry 1 to previous digit of list
            digits[idx] += 1
            return digits
        idx -= 1
    return [1] + digits


# digits = [9]
digits = [1, 2, 3]

print(plusOne(digits))