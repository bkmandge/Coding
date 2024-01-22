"""
                                Largest Number At Least Twice of Others

"""


def dominantIndex(nums):
    m = max(nums)
    i = nums.index(m)
    nums.remove(m)
    if 2 * max(nums) <= m:
        return i
    return -1


# nums = [1, 2, 3, 4]
nums = [3, 6, 1, 0]
print(dominantIndex(nums))