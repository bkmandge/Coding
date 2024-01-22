"""
                    Can Place Flowers
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Input: flowerbed = [0,0,1], n = 1
Output: True

"""


def canPlaceFlowers(flowerbed, n):  # n -> number of flowers to place
    # insert 0 to start & end of flowerbed
    f = [0] + flowerbed + [0]

    # start iteration from 1 to second last
    for i in range(1, len(f) - 1):
        if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
            f[i] = 1
            n = n - 1

    # check if all flowers placed or not
    if n <= 0:
        return True
    else:
        return False


flowerbed = [1, 0, 0, 1]
n = 1

print(canPlaceFlowers(flowerbed, n))
