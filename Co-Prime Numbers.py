"""
                    Coprime Number
-> If GCD of two numbers is 1 - then they are called as Coprime numbers
-> Non-prime numbers can be Coprime.
-> Prime numbers can not always be Coprime numbers

eg:- 21 and 22 are prime
21 -> 1, 3, 7
22 -> 1, 2, 11

16 & 25 are prime
16 -> 1, 2, 4, 8...
25 -> 1, 5, 25...

21 & 24 are not Coprime -> factor 3 is GCD of both
21 -> 1, 3, 7...(factors)
24 -> 1, 2, 3, 4....

"""


def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


def coPrime(num1, num2):
    if gcd(num1, num2) == 1:
        print("Coprime numbers!")
    else:
        print("Not coprime numbers!")


coPrime(21, 22)
coPrime(1, 3)
coPrime(21, 24)