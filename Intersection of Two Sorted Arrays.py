"""
                            Intersection of Two Sorted Arrays
Return elements present in both arrays, elements can be repeated,
but both arrays should have corresponding match of elements.


"""

# Brute Force

def intersection_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    visited_list = [0] * n2  # to keep track if elements visited or not

    intersected_arr = []
    for i in range(n1):
        for j in range(n2):
            if arr1[i] == arr2[j] and visited_list[j] == 0:
                intersected_arr.append(arr1[i])
                visited_list[j] = 1
                break
            if arr2[j] > arr1[i]:
                break

    return intersected_arr


arr1 = [1, 1, 2, 3, 4, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]

# print(intersection_arrays(arr1, arr2))


# Optimal Approach: Using two pointers O(n1 + n2), O(1)

def interseting_array(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = j = 0

    ans = []
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            ans.append(arr1[i])
            i += 1
            j += 1
    return ans


print(interseting_array(arr1, arr2))

