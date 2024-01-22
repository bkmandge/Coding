"""
                    Reverse Words in a String

Input: s = "the sky is blue"
Output: "blue is sky the"

"""


def reverse_words(s):
    result = ""
    i = 0
    n = len(s)

    while i < n:
        # to remove leading spaces
        while i < n and s[i] == " ":
            i = i + 1

        if i >= n:
            break

        # to get word until next space is found
        j = i + 1
        while j < n and s[j] != " ":
            j = j + 1

        # add word to substring
        substring = s[i:j]

        # if result str is empty then store substring in it else concatenate with earlier words in it
        if len(result) == 0:
            result = substring
        else:
            result = substring + " " + result

        # move i to next white space to loop again
        i = j + 1
    return result


str1 = "the sky is blue"
str2 = "hello world!"
print(reverse_words(str1))


# another way
"""
    # split given sentence into list
    s = s.split()

    # reverse list elements
    s = s[::-1]

    # join list back into original string format
    return " ".join(s)
"""