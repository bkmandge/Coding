"""
    To calculate power of any given number

"""
def power(base, expo):
    assert expo == int(expo), 'Exponent must be positive integer only!'
    if expo == 0:
        return 1
    if expo == 1:
        return base
    elif expo < 0:
        return 1 / base * power(base, expo + 1)
    else:
        return base * power(base, expo - 1)


print(power(-1, 2))  # negative base value
print(power(2, -1))  # negative exponent value
print(power(3.2, 2))  # float base value
print(power(2, 1.2))  # float exponent value