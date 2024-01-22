"""
                        Diagonal Traverse - 2 D Matrix

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105

"""


def findDiagonalOrder(mat):
    if not mat or not mat[0]:
        return []

    nums_rows = len(mat)
    nums_cols = len(mat[0])

    # creating diagonal lists for each diagonal, i.e. how many diagonals lists
    diagonals =[[] for _ in range(nums_rows + nums_cols - 1)]

    for i in range(nums_rows):
        for j in range(nums_cols):
            diagonals[i + j].append(mat[i][j])

    # store first diagonal result in res
    res = diagonals[0]

    # for other diagonal lists check if is is of odd diagonal number or even number
    # if even number reverse list
    for x in range(1, len(diagonals)):
        if x % 2 == 1:
            res.extend(diagonals[x])
        else:
            res.extend(diagonals[x][::-1])

    return res

