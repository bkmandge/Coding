"""
Decimal to Binary:- returns binary form of given decimal / integer number

1. get remainder of given number by 2
2. add 10 to it
3. recursively call decimalToBinary with dividing given num by 2

eg:- # 10 -> 1010, 2 -> 10

"""


def decimalToBinary(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * decimalToBinary(int(num / 2))


print(decimalToBinary(10))
print(decimalToBinary(2))