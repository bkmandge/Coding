"""
                Move Zeroes to Front of Array

"""
def move_zeroes(list1):
    start = 0
    end = len(list1) - 1

    while start <= end:
        if list1[start] != 0:
            list1[start], list1[end] = list1[end], list1[start]
        else:
            start += 1
            end -= 1
    return list1


lst = [1, 0, 1, 0, 1, 0]   # [0, 0, 0, 1, 1, 1]
print(move_zeroes(lst))
