"""
                        Max Number of K-Sum Pairs


"""


def maxOperations(nums, k):
    nums.sort()
    left = 0
    right = len(nums) - 1
    count = 0

    while left < right:
        if nums[left] + nums[right] == k:
            left += 1
            right -= 1
            count += 1
        elif nums[left] + nums[right] < k:
            left += 1
        else:
            right -= 1
    return count


nums = [1, 2, 3, 4]
nums1 = [3, 1, 3, 4, 3]
nums2 = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2

print(maxOperations(nums2, k))