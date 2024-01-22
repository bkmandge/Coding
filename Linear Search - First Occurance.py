"""
                            Linear Search - First Occurance

Start searching from beginning of array

"""


def searchFirstOccurance(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1


nums = [6, 7, 8, 4, 1]
target = 10

print(nums)
print(searchFirstOccurance(nums, target))