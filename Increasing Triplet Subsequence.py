"""
                    Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

"""


def increasingTriplets(nums):
    if len(nums) < 3:
        return False

    i = float("inf")
    j = float("inf")

    for index in range(len(nums)):
        # check if current element <= i, if yes assign it to i
        if nums[index] <= i:
            i = nums[index]
        # # else check if current element <= j, if yes assign it to j
        elif nums[index] <= j:
            j = nums[index]
        else:
            return True  # assigns next max value to k
    return False


nums = [2,1,5,0,4,6]

nums2 = [5,4,3,2,1]

nums3 = [1, 1, 1, 1, 1]

print(increasingTriplets(nums3))

