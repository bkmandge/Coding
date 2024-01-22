"""
1. Using if - else
2. Using max()
3. Using ternary operator
4. Using lambda()
5. Using sort() and return last element: [-1]
6. Using list comprehension

"""

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))

if num1 > num2:
    print(num1)
else:
    print(num2)
    

# max()
print(max(num1, num2))


# ternary operator
print(num1 if num1 > num2 else num2)


# lambda()
max_number = lambda num1, num2: num1 if num1 > num2 else num2
print(max_number(-1, 0))


# sort()
result = [num1, num2]
result.sort()
print(result[-1])


# list comprehension
max1 = [num1 if num1 > num2 else num2]
print(max1)