"""
GCD:- It is the largest positive integer that divides the numbers w/o a remainder.

eg:- 48, 12 = 6, 8, 12 = 4

"""
def gcd(a, b):
    assert int(a) == a and int(b) == b, 'Both numerator and denominator must be positive integers!'
    # if numerator / denominator is negative, convert them into positive int
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    # base condition
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(48, -18))