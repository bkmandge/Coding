"""
                    Prime Number
-> any number divided by 1 & itself only. 3, 5, 7, 11, 13...
-> 1 is not a prime number
-> loop(i) from 2 to given num, check if num % i, if yes break loop
         else return TRUE

"""

num = int(input("enter any number: "))

if num < 2:
    print("Not prime!")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime!")
            break
    else:
        print("Number is prime!")




