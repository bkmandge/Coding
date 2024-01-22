"""
                    Remove All Vowels from a String

Remove all vowels and return new string

Input: s = "leetcodeiscommunityforcoder"
Output: "ltcdscmmntyfrcdr"

"""


def remove_vowels(s):
    new_s = []

    # vowel dictionary, to store information about whether a given character is a vowel or not
    vowel_dict = {char: True for char in 'aeiou'}

    for ch in s:
        # if vowel_dict[ch] not in dict return False & add to new_s
        if not vowel_dict.get(ch, False):
            new_s.append(ch)
    return "".join(new_s)


s = "leetcodeiscommunityforcoder"
print(remove_vowels(s))