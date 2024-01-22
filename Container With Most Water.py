"""
                    Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

"""


def maxArea(height):
    # to store height result
    res = 0

    left = 0
    right = len(height) - 1

    while left < right:
        # calculate rectangle's area:- width * height
        area = (right - left) * min(height[left], height[right])

        # store result
        res = max(res, area)

        # if left height is min then water may slant so shift left to next height
        if height[left] < height[right]:
            left += 1
        else:
            # else shift right to prev height
            right -= 1
    return res


height = [1,8,6,2,5,4,8,3,7]

height2 = [1, 1]

print(maxArea(height2))
