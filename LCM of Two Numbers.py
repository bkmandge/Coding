"""
-> Lowest Common Multiple or Least Common Multiple
-> Find few multiples(multiplications of number * 1, number *2) & then find the least common one
-> LCM can not be smaller than given numbers
eg:- LCM of 2 & 3 is 6
2 -> 2, 4, 6, 8, 10..
3 -> 3, 6, 9, 12, 15...

-> num1 * num2 = LCM(num1 * num2) * GCD(num1 * num2)

-> LCM(num1* num2) = num1 * num2 // GCD(num1 * num2)
-> GCD(num2, num1 % num2)

"""


def GCD(num1, num2):
    if num1 < 0:
        num1 = num1 * -1
    if num2 < 0:
        num2 = num2 * -1
    if num2 == 0:
        return num1
    else:
        return GCD(num2, num1 % num2)


num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print(GCD(num1, num2))

lcm = num1 * num2 // GCD(num1, num2)
print(lcm)


# -----------------------------------------------------------------------------------------------
                                    ,,

def compute_LCM(num1, num2):
    if num1 > num2:
        higher = num1
    else:
        higher = num2
    value = higher

    while True:
        if higher % num1 == 0 and higher % num2 == 0:
            print("LCM of both numbers is: ", higher)
            break
        else:
            higher += value


compute_LCM(24, 36)
