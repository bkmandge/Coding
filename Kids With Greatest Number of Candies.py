"""
                    Kids With Greatest Number of Candies
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]

"""


def kidsWithCandies(candies, extraCandies):
    max_candy = max(candies)

    for i in range(len(candies)):
        if candies[i] + extraCandies >= max_candy:
            candies[i] = True
        else:
            candies[i] = False
    return candies


candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))