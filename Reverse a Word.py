"""
                    Reverse a Word

Input: s = "Hello"
Output: "olleh"

"""


def reverse_word(str):
    str1 = ""

    # iterate through given str & add it to str1
    for char in str:
        str1 = char + str1
    return str1


s = "hello"
print(reverse_word(s))

"""
Explanation:-
    iteration       char + str1  ->  o/p    
# 1st :-            "h" + ""     ->  "h"
# 2nd :-            "e" + "h"    ->  "eh"
# 3rd :-            "l" + "eh"   ->  "leh"
# 4th :-            "l" + "leh"  ->  "lleh"
# 5th :-            "o" + "lleh" ->  "olleh"

"""

# another way using slicing
print(s[::-1])
