# sentence = "thequickbrownfoxjumpsoverthelazydog"
# o/p:- True

# sentence = "leetcode"
# o/p:- False


def check_pangram(sentence):
    temp = set(sentence)
    # print(temp)
    if len(temp) == 26:
        return "Pangram"
    else:
        return "Not pangram"


sentence = "thequickbrownfoxjumpsoverthelazydog"
print(check_pangram(sentence))